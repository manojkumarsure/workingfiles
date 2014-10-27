-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Oct 09, 2014 at 03:12 PM
-- Server version: 5.5.38-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `university`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE IF NOT EXISTS `course` (
  `CourseId` char(6) NOT NULL,
  `cname` varchar(32) NOT NULL,
  `credits` tinyint(3) unsigned NOT NULL,
  `deptNo` tinyint(3) unsigned NOT NULL,
  UNIQUE KEY `CourseId` (`CourseId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE IF NOT EXISTS `department` (
  `DeptId` tinyint(3) unsigned NOT NULL,
  `Name` varchar(32) NOT NULL,
  `HOD` varchar(20) NOT NULL,
  `Phone` int(10) unsigned NOT NULL,
  UNIQUE KEY `DeptId` (`DeptId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `enrollment`
--

CREATE TABLE IF NOT EXISTS `enrollment` (
  `rollNo` char(8) NOT NULL,
  `CourseId` char(6) NOT NULL,
  `Sem` tinyint(3) unsigned NOT NULL,
  `year` int(4) unsigned NOT NULL,
  `Grade` char(1) NOT NULL,
  PRIMARY KEY (`rollNo`,`CourseId`,`Sem`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `prerequisite`
--

CREATE TABLE IF NOT EXISTS `prerequisite` (
  `PreReqCourse` char(6) NOT NULL,
  `CourseId` char(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `professor`
--

CREATE TABLE IF NOT EXISTS `professor` (
  `EmpId` char(6) NOT NULL,
  `Name` varchar(32) NOT NULL,
  `Sex` char(1) NOT NULL,
  `StartYear` smallint(5) unsigned NOT NULL,
  `DeptNo` tinyint(3) unsigned NOT NULL,
  `Phone` int(11) NOT NULL,
  UNIQUE KEY `EmpId` (`EmpId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `RollNo` char(8) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Degree` char(6) NOT NULL,
  `Year` smallint(6) NOT NULL,
  `Sex` char(1) NOT NULL,
  `DeptNo` tinyint(3) unsigned NOT NULL,
  `Advisor` varchar(6) NOT NULL,
  UNIQUE KEY `RollNo.` (`RollNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `teaching`
--

CREATE TABLE IF NOT EXISTS `teaching` (
  `EmpId` char(6) NOT NULL,
  `CourseId` char(6) NOT NULL,
  `Sem` tinyint(3) unsigned NOT NULL,
  `Year` int(4) unsigned NOT NULL,
  `ClassRoom` varchar(6) NOT NULL,
  PRIMARY KEY (`EmpId`,`CourseId`,`Sem`,`Year`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
