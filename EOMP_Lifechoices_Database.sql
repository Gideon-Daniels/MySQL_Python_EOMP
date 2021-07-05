-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: EOMP_Lifechoices_Database
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Admin`
--

DROP TABLE IF EXISTS `Admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Admin` (
  `Admin_rights` tinyint(1) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Surname` varchar(50) NOT NULL,
  `Phone_number` int NOT NULL,
  `ID_number` int NOT NULL,
  `Kin_phone_number` int NOT NULL,
  `User_in_building` tinyint(1) NOT NULL,
  PRIMARY KEY (`Admin_rights`),
  KEY `ID_number` (`ID_number`),
  KEY `Kin_phone_number` (`Kin_phone_number`),
  KEY `User_in_building` (`User_in_building`),
  CONSTRAINT `Admin_ibfk_1` FOREIGN KEY (`ID_number`) REFERENCES `User` (`Id_number`),
  CONSTRAINT `Admin_ibfk_2` FOREIGN KEY (`Kin_phone_number`) REFERENCES `Next_Of_Kin` (`Phone_number`),
  CONSTRAINT `Admin_ibfk_3` FOREIGN KEY (`User_in_building`) REFERENCES `User_In_Building` (`User_in_building`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin`
--

LOCK TABLES `Admin` WRITE;
/*!40000 ALTER TABLE `Admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `Admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Next_Of_Kin`
--

DROP TABLE IF EXISTS `Next_Of_Kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Next_Of_Kin` (
  `Phone_number` int NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Phone_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Next_Of_Kin`
--

LOCK TABLES `Next_Of_Kin` WRITE;
/*!40000 ALTER TABLE `Next_Of_Kin` DISABLE KEYS */;
/*!40000 ALTER TABLE `Next_Of_Kin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `Id_number` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Surname` varchar(50) NOT NULL,
  `Phone_number` int NOT NULL,
  `Kin_phone_number` int NOT NULL,
  `Admin_rights` tinyint(1) NOT NULL,
  `User_in_building` tinyint(1) NOT NULL,
  PRIMARY KEY (`Id_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_In_Building`
--

DROP TABLE IF EXISTS `User_In_Building`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_In_Building` (
  `User_in_building` tinyint(1) NOT NULL,
  `Time_signin` datetime NOT NULL,
  `Time_signout` datetime NOT NULL,
  PRIMARY KEY (`User_in_building`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_In_Building`
--

LOCK TABLES `User_In_Building` WRITE;
/*!40000 ALTER TABLE `User_In_Building` DISABLE KEYS */;
/*!40000 ALTER TABLE `User_In_Building` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-05 17:06:36
