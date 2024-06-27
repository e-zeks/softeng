-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: softeng
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
-- Table structure for table `user_logs`
--

DROP TABLE IF EXISTS `user_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_logs` (
  `LogID` int NOT NULL AUTO_INCREMENT,
  `EmployeeID` int DEFAULT NULL,
  `ClientID` int DEFAULT NULL,
  `UserType` enum('Employee','Client') NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Login_Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Logout_Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`LogID`),
  KEY `EmployeeID` (`EmployeeID`),
  KEY `ClientID` (`ClientID`),
  CONSTRAINT `user_logs_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employees` (`EmployeeID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_logs_ibfk_2` FOREIGN KEY (`ClientID`) REFERENCES `clients` (`ClientID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_logs`
--

LOCK TABLES `user_logs` WRITE;
/*!40000 ALTER TABLE `user_logs` DISABLE KEYS */;
INSERT INTO `user_logs` VALUES (1,1,NULL,'Employee','Admin','Account','2024-06-27 13:58:42','2024-06-27 13:58:42'),(2,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 13:59:51','2024-06-27 13:59:51'),(3,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 14:24:14','2024-06-27 14:24:14'),(4,1,NULL,'Employee','Admin','Account','2024-06-27 14:24:30','2024-06-27 14:24:30'),(5,1,NULL,'Employee','Admin','Account','2024-06-27 14:29:17','2024-06-27 14:29:17'),(6,1,NULL,'Employee','Admin','Account','2024-06-27 14:31:58','2024-06-27 14:31:58'),(7,1,NULL,'Employee','Admin','Account','2024-06-27 14:32:35','2024-06-27 14:32:35'),(8,1,NULL,'Employee','Admin','Account','2024-06-27 15:00:07','2024-06-27 15:00:07'),(9,1,NULL,'Employee','Admin','Account','2024-06-27 15:02:09','2024-06-27 15:02:09'),(10,1,NULL,'Employee','Admin','Account','2024-06-27 15:16:11','2024-06-27 15:16:11'),(11,1,NULL,'Employee','Admin','Account','2024-06-27 15:18:32','2024-06-27 15:18:32'),(12,1,NULL,'Employee','Admin','Account','2024-06-27 15:19:34','2024-06-27 15:19:34'),(13,1,NULL,'Employee','Admin','Account','2024-06-27 15:20:38','2024-06-27 15:20:38'),(14,1,NULL,'Employee','Admin','Account','2024-06-27 15:24:55','2024-06-27 15:24:55'),(15,1,NULL,'Employee','Admin','Account','2024-06-27 15:27:05','2024-06-27 15:27:05'),(16,1,NULL,'Employee','Admin','Account','2024-06-27 16:02:21','2024-06-27 16:02:21'),(17,1,NULL,'Employee','Admin','Account','2024-06-27 16:18:02','2024-06-27 16:18:02'),(18,1,NULL,'Employee','Admin','Account','2024-06-27 16:19:50','2024-06-27 16:19:50'),(19,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 16:25:15','2024-06-27 16:25:15'),(20,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 16:30:19','2024-06-27 16:30:19'),(21,1,NULL,'Employee','Admin','Account','2024-06-27 16:30:41','2024-06-27 16:30:41'),(22,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 16:31:39','2024-06-27 16:31:39'),(23,1,NULL,'Employee','Admin','Account','2024-06-27 16:34:00','2024-06-27 16:34:00'),(24,1,NULL,'Employee','Admin','Account','2024-06-27 16:35:42','2024-06-27 16:35:42'),(25,1,NULL,'Employee','Admin','Account','2024-06-27 16:41:25','2024-06-27 16:41:25'),(26,1,NULL,'Employee','Admin','Account','2024-06-27 17:18:39','2024-06-27 17:18:39'),(27,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 17:19:47','2024-06-27 17:19:47'),(28,1,NULL,'Employee','Admin','Account','2024-06-27 17:20:03','2024-06-27 17:20:03'),(29,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 17:20:21','2024-06-27 17:20:21'),(30,1,NULL,'Employee','Admin','Account','2024-06-27 17:31:23','2024-06-27 17:31:23'),(31,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 17:31:46','2024-06-27 17:31:46'),(32,1,NULL,'Employee','Admin','Account','2024-06-27 17:31:57','2024-06-27 17:31:57'),(33,1,NULL,'Employee','Admin','Account','2024-06-27 17:48:55','2024-06-27 17:48:55'),(34,1,NULL,'Employee','Admin','Account','2024-06-27 18:10:01','2024-06-27 18:10:01'),(35,1,NULL,'Employee','Admin','Account','2024-06-27 18:23:11','2024-06-27 18:23:11'),(36,1,NULL,'Employee','Admin','Account','2024-06-27 18:27:46','2024-06-27 18:27:46'),(37,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 18:57:12','2024-06-27 18:57:12'),(38,1,NULL,'Employee','Admin','Account','2024-06-27 19:15:54','2024-06-27 19:15:54'),(39,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 19:17:41','2024-06-27 19:17:41'),(40,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 19:18:36','2024-06-27 19:18:36'),(41,1,NULL,'Employee','Admin','Account','2024-06-27 19:19:10','2024-06-27 19:19:10'),(42,1,NULL,'Employee','Admin','Account','2024-06-27 19:22:28','2024-06-27 19:22:28'),(43,1,NULL,'Employee','Admin','Account','2024-06-27 19:23:41','2024-06-27 19:23:41'),(44,1,NULL,'Employee','Admin','Account','2024-06-27 19:25:32','2024-06-27 19:25:32'),(45,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 19:26:50','2024-06-27 19:26:50'),(46,1,NULL,'Employee','Admin','Account','2024-06-27 19:27:59','2024-06-27 19:27:59'),(47,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 19:28:06','2024-06-27 19:28:06'),(48,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 19:38:14','2024-06-27 19:38:14'),(49,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 19:56:51','2024-06-27 19:56:51'),(50,1,NULL,'Employee','Admin','Account','2024-06-27 19:57:32','2024-06-27 19:57:32'),(51,NULL,1,'Client','Myek Jego','Cruz','2024-06-27 20:01:17','2024-06-27 20:01:17');
/*!40000 ALTER TABLE `user_logs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-28  4:06:23
