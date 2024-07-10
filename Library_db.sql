CREATE DATABASE  IF NOT EXISTS `library` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `library`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `Username` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('Gayathri','@333');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `SlNo` int DEFAULT NULL,
  `BookName` varchar(100) DEFAULT NULL,
  `Genre` varchar(50) DEFAULT NULL,
  `Quantity` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Game Of thrones','Fantasy Novel',9),(2,'The Fellowship of the Ring','Fantasy Novel',10),(3,'The Lion The Witch And The Wardrobe','Fantasy Novel',10),(4,'The Colour Of The Magic','Fantasy Novel',10),(5,'Assassins Apprentice','Fantasy Novel',9),(6,'The Silence Of The Lambs','Thriller Novel',10),(7,'The Girl With The Dragon Tattoo','Thriller Novel',9),(8,'Da Vinci Code','Thriller Novel',10),(9,'Kiss The Girls','Thriller Novel',10),(10,'Gone Girl','Thriller Novel',10),(11,'Lord of Scoundrels','Romance Novel',10),(12,'The Bride','Romance Novel',10),(13,'Outlander','Romance Novel',10),(14,'Gone with the Wind','Romance Novel',10),(15,'Jane Eyre','Romance Novel',10),(16,'The Hitchhikers Guide to the Galaxy','Sci-Fi Novel',10),(17,'Brave New World','Sci-Fi Novel',10),(18,'Animal Farm','Sci-Fi Novel',10),(19,'Ready Player One','Sci-Fi Novel',10),(20,'The Time Machine','Sci-Fi Novel',10),(21,'The War of the Worlds','Horror Novel',9),(22,'The Shining','Horror Novel',10),(23,'Dracula','Horror Novel',10),(24,'The Haunting of Hill House','Horror Novel',10),(25,'Hell House','Horror Novel',10);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrow`
--

DROP TABLE IF EXISTS `borrow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrow` (
  `ID` int DEFAULT NULL,
  `Book_Borrowed` varchar(150) DEFAULT NULL,
  `date_of_borrowing` varchar(10) DEFAULT NULL,
  `SlNo` int DEFAULT NULL,
  KEY `ID` (`ID`),
  CONSTRAINT `borrow_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `membership` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow`
--

LOCK TABLES `borrow` WRITE;
/*!40000 ALTER TABLE `borrow` DISABLE KEYS */;
INSERT INTO `borrow` VALUES (1001,'Game Of thrones','2022-11-28',1),(1001,'Assassins Apprentice','2022-11-28',5),(1001,'The Girl With The Dragon Tattoo','2022-11-28',7),(1001,'The War of the Worlds','2022-11-28',21);
/*!40000 ALTER TABLE `borrow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membership`
--

DROP TABLE IF EXISTS `membership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membership` (
  `ID` int NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `PhNo` bigint DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Address` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membership`
--

LOCK TABLES `membership` WRITE;
/*!40000 ALTER TABLE `membership` DISABLE KEYS */;
INSERT INTO `membership` VALUES (1001,'Gayathri Jayan',8904481046,'gayatrijayan2003@gmail.com','#149, Harshitha Nilaya, Meenakshi Layout, Kalena Agrahara, Bannerghatta Road'),(1016,'Monki',456345,'sdfsd','fdasdf');
/*!40000 ALTER TABLE `membership` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-10 23:07:26
