from __future__ import annotations

import itertools

from database.database_config import create_connection
from psycopg2 import Error
from tqdm import tqdm
from transform import transform


def insert_data_from_dataframe(df):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        total_rows = len(df)
        progress_bar = tqdm(total=total_rows)

        batch_size = 50000  # Set the desired batch size

        # Create batches of rows for batch insertion
        rows_batches = [df[i:i + batch_size] for i in range(0, total_rows, batch_size)]

        # Start a transaction using the context manager
        with conn:
            for batch in rows_batches:
                rows = []
                for index, row in batch.iterrows():
                    # Create a tuple of values for each row
                    row_data = (
                        row['CodigoRegiao'], row['Regiao'],
                        row['CodigoTipoAtendimento'], row['DescricaoTipoAtendimento'],
                        row['CodigoAssunto'], row['DescricaoAssunto'], row['GrupoAssunto'],
                        row['CodigoProblema'], row['DescricaoProblema'], row['GrupoProblema'],
                        row['AnoAtendimento'], row['TrimestreAtendimento'], row['MesAtendimento'], row['DataAtendimento'],
                        row['UF'], row['SexoConsumidor'], row['FaixaEtariaConsumidor'], row['CEPConsumidor']
                    )
                    rows.append(row_data)

                # Insertion on table Regiao
                cursor.executemany("""
                    INSERT INTO Regiao (CodigoRegiao, Regiao)
                    VALUES (%s, %s)
                    ON CONFLICT (CodigoRegiao) DO NOTHING
                """, [(row[0], row[1]) for row in rows])

                # Insertion on table TipoAtendimento
                cursor.executemany("""
                    INSERT INTO TipoAtendimento (CodigoTipoAtendimento, DescricaoTipoAtendimento)
                    VALUES (%s, %s)
                    ON CONFLICT (CodigoTipoAtendimento) DO NOTHING
                """, [(row[2], row[3]) for row in rows])

                # Insertion on table Assunto
                cursor.executemany("""
                    INSERT INTO Assunto (CodigoAssunto, DescricaoAssunto, GrupoAssunto)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (CodigoAssunto) DO NOTHING
                """, [(row[4], row[5], row[6]) for row in rows])

                # Insertion on table Problema
                cursor.executemany("""
                    INSERT INTO Problema (CodigoProblema, DescricaoProblema, GrupoProblema)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (CodigoProblema) DO NOTHING
                """, [(row[7], row[8], row[9]) for row in rows])

                # Insertion on table Atendimento
                cursor.executemany("""
                    INSERT INTO Atendimento (AnoAtendimento, TrimestreAtendimento, MesAtendimento, DataAtendimento,
                                            CodigoRegiao, UF, CodigoTipoAtendimento, CodigoAssunto, CodigoProblema,
                                            SexoConsumidor, FaixaEtariaConsumidor, CEPConsumidor)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, [(row[10], row[11], row[12], row[13], row[0], row[14], row[2], row[4], row[7], row[15], row[16], row[17]) for row in rows])

                progress_bar.update(len(batch))

        progress_bar.close()
        print('Data copied successfully')

        return True

    except (Exception, Error) as error:
        print('Error while executing queries:', error)
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()
            print('Connection closed.')


# Set the desired values for year and trimester
year_values = range(2)
trimester_values = range(4)

# Create the connection outside the loop
conn = create_connection()

for year, trimester in itertools.product(year_values, trimester_values):
    df = transform(year_index=year, trimester_index=trimester + 1)
    insert_data_from_dataframe(df)

# Close the connection outside the loop
if conn:
    conn.close()
