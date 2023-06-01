# Здравствуйте, мои ответы на тестовые задания по SQL и PL/SQL, выполнялись задания через СУБД MySQL:
# 1) 1-ый вариант решения
SELECT name
FROM t_app_types
WHERE id != ALL(SELECT app_type_id
FROM t_applications
WHERE reg_date BETWEEN D1 AND D2);

# 2-ой вариант решения
SELECT name
FROM t_app_types
WHERE id NOT IN(SELECT app_type_id
FROM t_applications
WHERE reg_date BETWEEN D1 AND D2);

# 2) SELECT app_id, resp_dt, `code`, `text`
FROM t_resp
WHERE resp_dt > D1
ORDER BY resp_dt DESC
LIMIT 1;
