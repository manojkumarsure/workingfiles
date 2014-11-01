-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 29, 2014 at 10:03 PM
-- Server version: 5.5.40-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `supermarket`
--

-- --------------------------------------------------------

--
-- Table structure for table `Bill`
--

CREATE TABLE IF NOT EXISTS `Bill` (
  `BillNo.` int(8)  NULL,
  `CustId` int(8)  NULL,
  `SalsmnId` int(8)  NULL,
  `Date` date  NULL,
  `Time` time  NULL,
--   foreign key (SalsmnId) references salesman(SalsmnId) on delete set null on update cascade,
  UNIQUE KEY `BillNo.` (`BillNo.`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `check`
--

CREATE TABLE IF NOT EXISTS `check` (
  `CompId` int(8)  NULL,
  `Date` date  NULL,
  `SalsmnId` int(8)  NULL,
  UNIQUE KEY `CompId` (`CompId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `compliant`
--

CREATE TABLE IF NOT EXISTS `compliant` (
  `CompId` int(8)  NULL,
  `Date` date  NULL,
  `Type` char(8)  NULL,
  `Details` varchar(300)  NULL,
  `CustId` int(8)  NULL,
  UNIQUE KEY `CompId` (`CompId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE IF NOT EXISTS `Customer` (
  `CustId` int(8)  NULL,
  `Name` varchar(30)  NULL,
  `PhNo` char(14)  NULL,
  `Address` varchar(250)  NULL,
  UNIQUE KEY `CustId` (`CustId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Item`
--

CREATE TABLE IF NOT EXISTS `Item` (
  `ItemId` int(8) NULL,
  `Name` varchar(50)  NULL,
  `ManfDate` date  NULL,
  `ExpDate` date NULL,
  `Weight` decimal(8,3)  NULL,
  `Type` char(10)  NULL,
  `SupplierId` int(8)  NULL,
  `BillNo` int(8)  NULL,
  `MRP` decimal(6,2)  NULL,
  UNIQUE KEY `ItemId` (`ItemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Offer`
--

CREATE TABLE IF NOT EXISTS `Offer` (
  `ItemId` int(8)  NULL,
  `StDate` date  NULL,
  `EndDate` date  NULL,
  `Discount` int(8) NULL,
  UNIQUE KEY `ItemId` (`ItemId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `salesman`
--

CREATE TABLE IF NOT EXISTS `salesman` (
  `SalsmnId` int(8)  NULL,
  `Name` varchar(50) NULL,
  `Sex` char(1)  NULL,
  `Address` varchar(50) NULL,
  UNIQUE KEY `SalsmnId` (`SalsmnId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Supplier`
--

CREATE TABLE IF NOT EXISTS `Supplier` (
  `SupplierId` int(8) NULL,
  `Name` varchar(50)  NULL,
  `Address` varchar(250)  NULL,
  UNIQUE KEY `SupplierId` (`SupplierId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
