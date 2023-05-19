CREATE DATABASE db_vacancies
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Russian_Russia.1251'
    LC_CTYPE = 'Russian_Russia.1251'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

---------------

CREATE TABLE IF NOT EXISTS public.companies
(
    id integer NOT NULL,
    name text COLLATE pg_catalog."default",
    CONSTRAINT companies_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.companies
    OWNER to postgres;


---------



CREATE TABLE IF NOT EXISTS public.vacancies
(
    id integer NOT NULL,
    url text COLLATE pg_catalog."default",
    job_name text COLLATE pg_catalog."default",
    salary_from integer,
    salary_to integer,
    employer_id integer NOT NULL,
    CONSTRAINT vacancies_pkey PRIMARY KEY (id),
    CONSTRAINT vacancies_employer_id_fkey FOREIGN KEY (employer_id)
        REFERENCES public.companies (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vacancies
    OWNER to postgres;