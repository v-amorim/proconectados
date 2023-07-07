-- Table: Atendimento
CREATE TABLE Atendimento (
	IDAtendimento SERIAL PRIMARY KEY,
	AnoAtendimento INT,
	TrimestreAtendimento INT,
	MesAtendimento INT,
	DataAtendimento DATE,
	CodigoRegiao VARCHAR(2),
	UF VARCHAR(2),
	CodigoTipoAtendimento INT,
	CodigoAssunto INT,
	CodigoProblema INT,
	SexoConsumidor CHAR(1),
	FaixaEtariaConsumidor VARCHAR,
	CEPConsumidor VARCHAR
);
-- Table: Regiao
CREATE TABLE Regiao (
	CodigoRegiao VARCHAR(2) PRIMARY KEY,
	Regiao VARCHAR(15)
);
-- Table: TipoAtendimento
CREATE TABLE TipoAtendimento (
	CodigoTipoAtendimento INT PRIMARY KEY,
	DescricaoTipoAtendimento VARCHAR
);
-- Table: Assunto
CREATE TABLE Assunto (
	CodigoAssunto INT PRIMARY KEY,
	DescricaoAssunto VARCHAR,
	GrupoAssunto VARCHAR
);
-- Table: Problema
CREATE TABLE Problema (
	CodigoProblema INT PRIMARY KEY,
	DescricaoProblema VARCHAR,
	GrupoProblema VARCHAR
);
-- Alter table: Atendimento
ALTER TABLE Atendimento
ADD CONSTRAINT fk_Atendimento_Regiao FOREIGN KEY (CodigoRegiao) REFERENCES Regiao(CodigoRegiao);
ALTER TABLE Atendimento
ADD CONSTRAINT fk_Atendimento_TipoAtendimento FOREIGN KEY (CodigoTipoAtendimento) REFERENCES TipoAtendimento(CodigoTipoAtendimento);
ALTER TABLE Atendimento
ADD CONSTRAINT fk_Atendimento_Assunto FOREIGN KEY (CodigoAssunto) REFERENCES Assunto(CodigoAssunto);
ALTER TABLE Atendimento
ADD CONSTRAINT fk_Atendimento_Problema FOREIGN KEY (CodigoProblema) REFERENCES Problema(CodigoProblema);
