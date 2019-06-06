BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "mensagens" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"idUsuario"	INTEGER,
	"texto"	TEXT,
	"criado_em"	DATE,
	"mencionados"	TEXT,
	"likes"	INTEGER DEFAULT 0,
	"deslikes"	INTEGER DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "men" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"idUsuarioEnviado"	INTEGER,
	"idUsuarioRecebido"	INTEGER,
	"mensagem"	TEXT,
	"criado_em"	DATE
);
CREATE TABLE IF NOT EXISTS "seguidores" (
	"idUsuario"	INTEGER,
	"idSeguidor"	INTEGER
);
CREATE TABLE IF NOT EXISTS "usuarios" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"nome"	TEXT NOT NULL,
	"login"	TEXT NOT NULL,
	"senha"	VARCHAR(20) NOT NULL,
	"email"	TEXT NOT NULL,
	"criado_em"	DATE NOT NULL
);
INSERT INTO "mensagens" VALUES (1,1,'isso é so um teste viu, tenha calma xD xD',NULL,NULL,NULL,NULL);
INSERT INTO "mensagens" VALUES (2,3,'vamos brincar de testar isso ?',NULL,NULL,NULL,NULL);
INSERT INTO "mensagens" VALUES (3,20,'dklskdslkdslkdlskdslk','2019-06-05 11:00:03.907814',NULL,NULL,NULL);
INSERT INTO "mensagens" VALUES (4,1,'isso é so um teste viu, tenha calma xD xD','2019-06-05 11:00:03.907814',NULL,NULL,NULL);
INSERT INTO "mensagens" VALUES (5,20,'tekdksldkslkdslk','2019-06-20 11:00:03.907814',NULL,NULL,NULL);
INSERT INTO "mensagens" VALUES (6,20,'vamos testar','2019-06-05 10:00:03.907814',NULL,NULL,NULL);
INSERT INTO "mensagens" VALUES (7,1,'dkslkdsldskll','2019-06-05 14:49:21.545498','fontes,lucas',-44,0);
INSERT INTO "men" VALUES (1,100,100,'testando o envio de mensagem','2019-06-05 11:38:29.414406');
INSERT INTO "men" VALUES (2,100,100,'testando o envio de mensagem','2019-06-05 13:42:03.171277');
INSERT INTO "men" VALUES (3,1,3,'esse e um teste de mensagem','2019-06-05 13:42:30.376645');
INSERT INTO "men" VALUES (4,1,3,'vamos testar','2019-06-05 13:53:55.883299');
INSERT INTO "men" VALUES (5,20,1,'vamos testar','2019-06-05 13:56:17.468682');
INSERT INTO "men" VALUES (6,20,1,'luvasklakslakskas','2019-06-05 13:58:21.451477');
INSERT INTO "men" VALUES (7,20,1,'ldksldksldkslkdsdks','2019-06-05 14:00:39.251002');
INSERT INTO "men" VALUES (8,20,1,'ldksldksldkslkdskds','2019-06-05 14:04:13.910285');
INSERT INTO "seguidores" VALUES (1,20);
INSERT INTO "seguidores" VALUES (3,4);
INSERT INTO "seguidores" VALUES (3,4);
INSERT INTO "seguidores" VALUES (3,4);
INSERT INTO "seguidores" VALUES (3,5);
INSERT INTO "usuarios" VALUES (1,'lucas','lucas001','lucas123','lucas@gmail.com','1998-05-12');
INSERT INTO "usuarios" VALUES (2,'lucas','lucas000001','lucas111112','lucasfontes@gmail.com','1998-05-12');
INSERT INTO "usuarios" VALUES (3,'lucas','fontes','fontes001','fontes@gmail.com','1998-05-12');
INSERT INTO "usuarios" VALUES (4,'cartaxo','cartaxo1','cartaxo001','cartaxo@gmail.com','2019-06-04 17:30:02.773397');
INSERT INTO "usuarios" VALUES (5,'samuel1','samuel','samuel001','samuel@samuel.com','2019-06-04 17:42:05.919945');
INSERT INTO "usuarios" VALUES (6,'samuel1','samuel','samuel001','samuel@samuel.com','2019-06-04 17:42:36.951795');
INSERT INTO "usuarios" VALUES (7,'samuel1','samuel','samuel001','samuel@samuel.com','2019-06-04 17:42:58.767621');
INSERT INTO "usuarios" VALUES (8,'adriel1','adriel','adriel001','adriel@adriel.com','2019-06-04 17:43:41.471135');
INSERT INTO "usuarios" VALUES (9,'maycon1','maycon','maycon001','maycon@maycon.com','2019-06-04 17:45:36.062475');
INSERT INTO "usuarios" VALUES (10,'maycon1','maycon','maycon001','maycon@maycon.com','2019-06-04 17:47:07.693625');
INSERT INTO "usuarios" VALUES (11,'teste','teste','teste','teste','2019-06-04 17:48:20.341183');
INSERT INTO "usuarios" VALUES (12,'teste','teste','teste','teste','2019-06-04 17:48:46.397006');
INSERT INTO "usuarios" VALUES (13,'stardeath','vader','vader001','vader@vader.com','2019-06-05 13:43:25.110794');
INSERT INTO "usuarios" VALUES (20,'test','testando','testando','','');
INSERT INTO "usuarios" VALUES (21,'lskd','ldksldkskd','sdlks','dlksk','2019-06-05 15:09:06.073277');
COMMIT;
