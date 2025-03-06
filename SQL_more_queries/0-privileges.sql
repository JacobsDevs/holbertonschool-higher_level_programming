-- Show the privileges of user_0d_1 and user_0d_2
SELECT *
FROM information_schema.user_privileges
WHERE GRANTEE in ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'");
