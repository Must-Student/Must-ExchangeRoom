-- MySQL dump 10.14  Distrib 5.5.65-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: ExchangeRoom
-- ------------------------------------------------------
-- Server version	5.5.65-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AccountInfo`
--

DROP TABLE IF EXISTS `AccountInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AccountInfo` (
  `EmailAddress` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `UserName` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `ContactInfo` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `SystemFind` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `SelfFind` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `MyDeal` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `PassWord` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `IsVerified` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `Md5` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `Sex` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `Address` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `Model` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `IdealAddress` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `IdealModel` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `Note` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `AssociateEmail` varchar(255) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AccountInfo`
--

LOCK TABLES `AccountInfo` WRITE;
/*!40000 ALTER TABLE `AccountInfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `AccountInfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-22  3:26:01
