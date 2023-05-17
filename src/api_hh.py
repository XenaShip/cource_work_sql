import requests


class JobAPI:
    """абстрактный класс для хранения информации из API"""
    def __init__(self):
        pass

    def get_vacancies(self, name_job):
        pass


class HeadHunterAPI(JobAPI):
    "класс для хранения информации из API с сайта HH"
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name_job, pages):
        "хранение вакансий в привычном виде"
        url = self.url
        ans_vacancies = []
        ans_companies = {}
        for i in range(pages):
            par = {'text': name_job, 'per_page': '50', 'page': i}
            r = requests.get(url, params=par)
            e = r.json()
            for j in e['items']:
                job_id = j['id']
                job_url = j['alternate_url']
                job_name = j['name']
                try:
                    if not((j['salary'] is None) or (j['salary']['from'] is None)):
                        salary_from = j['salary']['from']
                        salary_to = j['salary']['to']
                    else:
                        salary_from = 0
                        salary_to = 0
                    employer_id = j['employer']['id']
                except KeyError:
                    continue
                employer_name = j['employer']['name']
                vacanc = (job_id, job_url, job_name, salary_from, salary_to, employer_id)
                company = (employer_id, employer_name)
                ans_companies[employer_id] = company[1]
                ans_vacancies.append(vacanc)
        return list(ans_companies.items()), ans_vacancies
