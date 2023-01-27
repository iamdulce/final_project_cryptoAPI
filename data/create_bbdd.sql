CREATE TABLE "movements" (
	"id"	INTEGER,
	"date"	TEXT NOT NULL,
	"time"	TEXT NOT NULL,
	"from_coin"	TEXT NOT NULL,
	"from_quantity"	REAL NOT NULL,
	"to_coin"	TEXT NOT NULL,
	"to_quantity"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);