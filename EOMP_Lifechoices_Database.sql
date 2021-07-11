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
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `cell_num` int NOT NULL,
  `kin_number` int NOT NULL,
  `admin_rights` tinyint(1) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`admin_rights`),
  KEY `admin_id` (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin`
--

LOCK TABLES `Admin` WRITE;
/*!40000 ALTER TABLE `Admin` DISABLE KEYS */;
INSERT INTO `Admin` VALUES (1,'Gideon','Daniels',726078261,726075263,1,'gideon');
/*!40000 ALTER TABLE `Admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Attendance_register`
--

DROP TABLE IF EXISTS `Attendance_register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Attendance_register` (
  `user_id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `date_signed_in` date DEFAULT NULL,
  `time_signed_in` time NOT NULL,
  `time_sign_out` time NOT NULL,
  KEY `user_id` (`user_id`),
  CONSTRAINT `Attendance_register_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Attendance_register`
--

LOCK TABLES `Attendance_register` WRITE;
/*!40000 ALTER TABLE `Attendance_register` DISABLE KEYS */;
INSERT INTO `Attendance_register` VALUES (2,'Gilbert','2021-07-11','09:19:04','09:22:29'),(1,'Gideon','2021-07-11','09:24:41','09:26:30');
/*!40000 ALTER TABLE `Attendance_register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Log_in_details`
--

DROP TABLE IF EXISTS `Log_in_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Log_in_details` (
  `user_id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  KEY `user_id` (`user_id`),
  CONSTRAINT `Log_in_details_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Log_in_details`
--

LOCK TABLES `Log_in_details` WRITE;
/*!40000 ALTER TABLE `Log_in_details` DISABLE KEYS */;
INSERT INTO `Log_in_details` VALUES (1,'Gideon','gideon'),(2,'Gilbert','gilbert'),(3,'Merlin','merlin');
/*!40000 ALTER TABLE `Log_in_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Next_of_kin`
--

DROP TABLE IF EXISTS `Next_of_kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Next_of_kin` (
  `user_id` int NOT NULL,
  `username` varchar(50) NOT NULL,
  `cell_number` int NOT NULL,
  KEY `user_id` (`user_id`),
  CONSTRAINT `Next_of_kin_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Next_of_kin`
--

LOCK TABLES `Next_of_kin` WRITE;
/*!40000 ALTER TABLE `Next_of_kin` DISABLE KEYS */;
INSERT INTO `Next_of_kin` VALUES (1,'Merlin',726075263),(2,'Gideon',726078261),(3,'gilbert',725558888);
/*!40000 ALTER TABLE `Next_of_kin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `cell_num` int NOT NULL,
  `kin_number` int NOT NULL,
  `admin_rights` tinyint(1) NOT NULL,
  `password` varchar(50) NOT NULL,
  `user_id_number` varchar(13) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Gideon','Daniels',726078261,726075263,1,'gideon','9609075272087'),(2,'Gilbert','Daniels',725558888,726078261,0,'gilbert','9609075272086'),(3,'Merlin','Daniels',729997777,726078261,0,'merlin','206095272113');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11  9:41:55
