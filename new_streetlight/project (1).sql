-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 28, 2024 at 01:16 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `esp32_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE `project` (
  `time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `id` varchar(50) NOT NULL,
  `val1` int(50) NOT NULL,
  `val2` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`time`, `id`, `val1`, `val2`) VALUES
('2024-07-27 23:13:55', 'Pole3', 1, 1),
('2024-07-27 23:13:56', 'Pole1', 0, 1),
('2024-07-27 23:13:57', 'Pole2', 1, 1),
('2024-07-27 23:14:02', 'Pole3', 1, 1),
('2024-07-27 23:14:03', 'Pole2', 1, 1),
('2024-07-27 23:14:05', 'Pole2', 1, 1),
('2024-07-27 23:14:09', 'Pole3', 1, 1),
('2024-07-27 23:14:11', 'Pole2', 1, 1),
('2024-07-27 23:14:13', 'Pole2', 1, 1),
('2024-07-27 23:14:50', 'Pole3', 1, 1),
('2024-07-27 23:14:52', '', 1, 1),
('2024-07-27 23:14:53', 'Pole1', 0, 1),
('2024-07-27 23:14:57', 'Pole3', 1, 1),
('2024-07-27 23:14:59', 'Pole2', 1, 1),
('2024-07-27 23:15:00', 'Pole1', 0, 1),
('2024-07-27 23:15:05', 'Pole3', 1, 1),
('2024-07-27 23:15:06', 'Pole2', 1, 1),
('2024-07-27 23:15:07', 'Pole2', 1, 1),
('2024-07-27 23:16:25', 'Pole3', 1, 1),
('2024-07-27 23:16:26', 'Pole1', 0, 1),
('2024-07-27 23:16:28', 'Pole2', 1, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
