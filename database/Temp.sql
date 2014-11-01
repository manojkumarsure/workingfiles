-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 29, 2014 at 10:49 PM
-- Server version: 5.5.40-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Temp`
--

-- --------------------------------------------------------

--
-- Table structure for table `Bill`
--

CREATE TABLE IF NOT EXISTS `Bill` (
  `BillNo.` int(8) DEFAULT NULL,
  `CustId` int(8) DEFAULT NULL,
  `SalsmnId` int(8) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` time DEFAULT NULL,
  UNIQUE KEY `BillNo.` (`BillNo.`),
  KEY `SalsmnId` (`SalsmnId`),
  KEY `CustId` (`CustId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `check`
--

CREATE TABLE IF NOT EXISTS `check` (
  `CompId` int(8) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `SalsmnId` int(8) DEFAULT NULL,
  UNIQUE KEY `CompId` (`CompId`),
  KEY `SalsmnId` (`SalsmnId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `compliant`
--

CREATE TABLE IF NOT EXISTS `compliant` (
  `CompId` int(8) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Type` char(8) DEFAULT NULL,
  `Details` varchar(300) DEFAULT NULL,
  `CustId` int(8) DEFAULT NULL,
  UNIQUE KEY `CompId` (`CompId`),
  KEY `CustId` (`CustId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE IF NOT EXISTS `Customer` (
  `CustId` int(8) DEFAULT NULL,
  `Name` varchar(30) DEFAULT NULL,
  `PhNo` char(14) DEFAULT NULL,
  `Address` varchar(250) DEFAULT NULL,
  UNIQUE KEY `CustId` (`CustId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Item`
--

CREATE TABLE IF NOT EXISTS `Item` (
  `ItemId` int(8) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `ManfDate` date DEFAULT NULL,
  `ExpDate` date DEFAULT NULL,
  `Weight` decimal(8,3) DEFAULT NULL,
  `Type` char(10) DEFAULT NULL,
  `SupplierId` int(8) DEFAULT NULL,
  `BillNo` int(8) DEFAULT NULL,
  `MRP` decimal(6,2) DEFAULT NULL,
  UNIQUE KEY `ItemId` (`ItemId`),
  KEY `SupplierId` (`SupplierId`),
  KEY `BillNo` (`BillNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Offer`
--

CREATE TABLE IF NOT EXISTS `Offer` (
  `ItemId` int(8) DEFAULT NULL,
  `StDate` date DEFAULT NULL,
  `EndDate` date DEFAULT NULL,
  `Discount` int(8) DEFAULT NULL,
  UNIQUE KEY `ItemId` (`ItemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `salesman`
--

CREATE TABLE IF NOT EXISTS `salesman` (
  `SalsmnId` int(8) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Sex` char(1) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  UNIQUE KEY `SalsmnId` (`SalsmnId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Supplier`
--

CREATE TABLE IF NOT EXISTS `Supplier` (
  `SupplierId` int(8) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Address` varchar(250) DEFAULT NULL,
  UNIQUE KEY `SupplierId` (`SupplierId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Bill`
--
ALTER TABLE `Bill`
  ADD CONSTRAINT `Bill_ibfk_2` FOREIGN KEY (`CustId`) REFERENCES `Customer` (`CustId`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `Bill_ibfk_1` FOREIGN KEY (`SalsmnId`) REFERENCES `salesman` (`SalsmnId`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `check`
--
ALTER TABLE `check`
  ADD CONSTRAINT `check_ibfk_2` FOREIGN KEY (`SalsmnId`) REFERENCES `salesman` (`SalsmnId`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `check_ibfk_1` FOREIGN KEY (`CompId`) REFERENCES `compliant` (`CompId`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `compliant`
--
ALTER TABLE `compliant`
  ADD CONSTRAINT `compliant_ibfk_1` FOREIGN KEY (`CustId`) REFERENCES `Customer` (`CustId`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `Item`
--
ALTER TABLE `Item`
  ADD CONSTRAINT `Item_ibfk_2` FOREIGN KEY (`BillNo`) REFERENCES `Bill` (`BillNo.`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `Item_ibfk_1` FOREIGN KEY (`SupplierId`) REFERENCES `Supplier` (`SupplierId`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `Offer`
--
ALTER TABLE `Offer`
  ADD CONSTRAINT `Offer_ibfk_1` FOREIGN KEY (`ItemId`) REFERENCES `Item` (`ItemId`) ON DELETE SET NULL ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
