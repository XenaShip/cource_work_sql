import psycopg2


class DBManager:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="db_vacancies",
            user="postgres",
            password="Xena2003"
        )

    def close(self):
        self.connection.close()

    def clean(self):
        with self.connection.cursor() as cur:
            cur.execute("truncate companies cascade")
        self.connection.commit()

    def add_companies(self, companies):
        with self.connection.cursor() as cur:
            for i in companies:
                cur.execute("INSERT INTO companies (id, name) VALUES (%s, %s)", i)
        self.connection.commit()

    @staticmethod
    def db_testing(companies):
        db_test = DBManager()
        db_test.add_companies(companies)
        db_test.close()

    def add_vacancies(self, vacancies):
        with self.connection.cursor() as cur:
            for i in vacancies:
                cur.execute("INSERT INTO vacancies (id, url, job_name, salary_from, salary_to, employer_id) VALUES (%s, %s, %s, %s, %s, %s)", i)
        self.connection.commit()

    def get_companies_and_vacancies_count(self):
        with self.connection.cursor() as cur:
            cur.execute("select companies.name, count(vacancies.employer_id) from companies join vacancies on vacancies.employer_id = companies.id group by companies.name order by count(vacancies) desc")
            rows = cur.fetchall()
            return rows

    def get_all_vacancies(self):
        with self.connection.cursor() as cur:
            cur.execute("select vacancies.job_name, companies.name, vacancies.salary_from, vacancies.url from companies, vacancies")
            rows = cur.fetchall()
            return rows

    def get_avg_salary(self):
        with self.connection.cursor() as cur:
            cur.execute("select sum(salary_from) from vacancies where salary_from <> 0")
            rows1 = list(cur.fetchall())
            cur.execute("select count(salary_from) from vacancies where salary_from <> 0")
            rows2 = list(cur.fetchall())
            ans = rows1[0][0] / rows2[0][0]
            return ans

    def get_vacancies_with_higher_salary(self):
        with self.connection.cursor() as cur:
            cur.execute("select job_name from vacancies where salary_from > %s", (self.get_avg_salary(),))
            rows = cur.fetchall()
            return rows

    def get_vacancies_with_keyword(self, k_word):
        k_word = k_word.lower()
        k_word_in_beg = '%' + k_word.capitalize() + '%'
        with self.connection.cursor() as cur:
            cur.execute("select job_name from vacancies where job_name like %s or job_name like %s", ('%' + k_word + '%', k_word_in_beg))
            rows = cur.fetchall()
            return rows
