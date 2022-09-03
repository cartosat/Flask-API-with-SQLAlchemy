-- --------------------------------------------------------
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
-- Generation Time: Sept 03, 2022 at 03:30 PM
-- Host: localhost    Database: virtual_studio
-- Server version	8.0.29
-- --------------------------------------------------------

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+05:30";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- --------------------------------------------------------
--
-- Creat Database: `virtual_studio`
-- 
-- --------------------------------------------------------

CREATE DATABASE virtual_studio;
USE virtual_studio;

-- --------------------------------------------------------
--
-- Table structure for table `tbl_admin`
--
-- --------------------------------------------------------

CREATE TABLE `tbl_admin` (
  `id` int(10) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `photo` varchar(255) NOT NULL,
  `role` varchar(30) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbl_admin`
--

INSERT INTO `tbl_admin` (`id`, `full_name`, `email`, `phone`, `password`, `photo`, `role`, `status`) VALUES
(101, 'Vaibhav Wagaskar', 'cartosat4@gmail.com', '7447359256', 'f91e15dbec69fc40f81f0876e7009648', 'admin-101.jpg', 'Super Admin', 'Active'),
(104, 'Swaraj Gore', 'swarajgo@gmail.com', '49857243857', 'f91e15dbec69fc40f81f0876e7009648', 'admin-104.jpg', 'Admin', 'Active'),
(107, 'Suyash Lokhande', 'suyashlokhande@gmail.com', '7775058892', 'f91e15dbec69fc40f81f0876e7009648', 'admin-104.jpg', 'Admin', 'Active');

-- --------------------------------------------------------

--
-- Indexes for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

COMMIT;