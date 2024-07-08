-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: softeng
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `sessions`
--

DROP TABLE IF EXISTS `sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sessions` (
  `SessionID` int NOT NULL AUTO_INCREMENT,
  `BookingID` int DEFAULT NULL,
  `Day` varchar(50) DEFAULT NULL,
  `StartTime` varchar(45) DEFAULT NULL,
  `EndTime` varchar(45) DEFAULT NULL,
  `Status` enum('Completed','Cancelled','Not Done') NOT NULL DEFAULT 'Not Done',
  `Session_Counter` int DEFAULT '0',
  PRIMARY KEY (`SessionID`),
  KEY `BookingID` (`BookingID`),
  CONSTRAINT `sessions_ibfk_1` FOREIGN KEY (`BookingID`) REFERENCES `booking` (`BookingID`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessions`
--

LOCK TABLES `sessions` WRITE;
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
INSERT INTO `sessions` VALUES (1,1,'Sunday','8:00 AM','9:00 AM','',0),(2,1,'Monday','9:00 AM','10:00 AM','',0),(3,2,'Monday','7:00 AM','8:00 AM','',0),(4,2,'Wednesday','7:00 AM','8:00 AM','',0),(5,2,'Friday','7:00 AM','8:00 AM','',0),(6,3,'Monday','7:00 AM','8:00 AM','',0),(7,3,'Wednesday','7:00 AM','8:00 AM','',0),(8,3,'Friday','7:00 AM','8:00 AM','',0),(9,4,'Monday','7:00 AM','8:00 AM','',0),(10,4,'Wednesday','7:00 AM','8:00 AM','',0),(11,4,'Friday','7:00 AM','8:00 AM','',0),(12,6,'Monday','8:00 AM','9:00 AM','',0),(13,7,'Wednesday','7:00 AM','8:00 AM','',0),(14,8,'Monday','7:00 AM','8:00 AM','',0),(15,8,'Wednesday','8:00 AM','9:00 AM','',0),(16,9,'Wednesday','8:00 AM','9:00 AM','',0),(17,10,'Monday','8:00 AM','9:00 AM','',0),(18,10,'Wednesday','8:00 AM','9:00 AM','',0),(19,11,'Monday','10:00 AM','11:00 AM','Not Done',3),(20,11,'Tuesday','10:00 AM','11:00 AM','Not Done',3),(21,12,'Monday','10:00 AM','11:00 AM','Not Done',0),(22,12,'Tuesday','10:00 AM','11:00 AM','Not Done',0),(23,13,'Monday','10:00 AM','11:00 AM','Not Done',3),(24,13,'Tuesday','10:00 AM','11:00 AM','Not Done',3),(25,14,'Monday','7:00 AM','8:00 AM','Not Done',0),(26,15,'Wednesday','9:00 AM','10:00 AM','Not Done',0),(27,16,'Wednesday','8:00 AM','9:00 AM','Not Done',0),(28,17,'Thursday','8:00 AM','9:00 AM','Not Done',0),(29,18,'Monday','1:00 PM','2:00 PM','Not Done',0),(30,18,'Wednesday','12:00 PM','1:00 PM','Not Done',0),(31,18,'Friday','6:00 PM','7:00 PM','Not Done',0),(32,18,'Saturday','3:00 PM','4:00 PM','Not Done',0),(33,19,'Wednesday','8:00 AM','9:00 AM','Not Done',0),(34,21,'Tuesday','8:00 AM','9:00 AM','Not Done',8);
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-09  1:29:02
