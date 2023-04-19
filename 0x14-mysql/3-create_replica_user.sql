-- Create a MySQL user named replica_user on both web-01 and web-02
-- +with the host name set to %
-- +and the password alx-123qwe
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'alx-123qwe';
 GRANT REPLICATION SLAVE ON * . * TO 'replica_user'@'%';
 GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
 FLUSH PRIVILEGES;
