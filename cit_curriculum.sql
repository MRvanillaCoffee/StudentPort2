-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 07, 2026 at 05:32 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cit_curriculum`
--

-- --------------------------------------------------------

--
-- Table structure for table `clos`
--

CREATE TABLE `clos` (
  `id` int(11) NOT NULL,
  `course_id` int(11) DEFAULT NULL,
  `clo_code` varchar(20) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `clos`
--

INSERT INTO `clos` (`id`, `course_id`, `clo_code`, `description`) VALUES
(1, 1, 'CLO 1', 'อธิบายหลักการทำงานของการเขียนโปรแกรมได้'),
(2, 1, 'CLO 2', 'เขียนและทดสอบโปรแกรมเบื้องต้นได้'),
(3, 2, 'CLO 1', 'ติดตั้งและใช้งาน Linux เบื้องต้น'),
(4, 2, 'CLO 2', 'บริหารจัดการระบบและผู้ใช้งานได้'),
(5, 3, 'CLO 1', 'ออกแบบ E-R Diagram ได้'),
(6, 3, 'CLO 2', 'เขียนคำสั่ง SQL พื้นฐานได้'),
(7, 4, 'CLO 1', 'อธิบายหลักการรักษาความปลอดภัยเครือข่าย'),
(8, 4, 'CLO 2', 'ตั้งค่า Firewall เบื้องต้นได้'),
(9, 5, 'CLO 1', 'วิเคราะห์และออกแบบระบบซอฟต์แวร์'),
(10, 6, 'CLO 1', 'พัฒนาหน้าเว็บด้วย HTML/CSS/Vue.js ได้');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `id` int(11) NOT NULL,
  `course_code` varchar(20) DEFAULT NULL,
  `name_th` varchar(150) DEFAULT NULL,
  `name_en` varchar(150) DEFAULT NULL,
  `section` varchar(10) DEFAULT NULL,
  `academic_year` int(11) DEFAULT NULL,
  `credits` varchar(20) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `description_en` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`id`, `course_code`, `name_th`, `name_en`, `section`, `academic_year`, `credits`, `description`, `description_en`) VALUES
(1, '030513101', 'การเขียนโปรแกรมคอมพิวเตอร์', 'COMPUTER PROGRAMMING', '1', 2568, '3(2-2-5)', 'ศึกษาหลักการและกระบวนการเขียนโปรแกรมคอมพิวเตอร์ ชนิดข้อมูล ตัวแปร นิพจน์ โครงสร้างควบคุม ฟังก์ชัน แถวลำดับ การจัดการข้อผิดพลาด และการประยุกต์ใช้งานเบื้องต้น', 'Study of principles and processes of computer programming, data types, variables, expressions, control structures, functions, arrays, error handling, and basic applications.'),
(2, '030523126', 'ระบบปฏิบัติการลีนุกซ์และการบริหารจัดการ', 'LINUX OPERATING SYS & ADMIN', '1', 2568, '3(2-2-5)', 'ศึกษาและปฏิบัติการติดตั้งระบบปฏิบัติการลีนุกซ์ การบริหารจัดการผู้ใช้งานและสิทธิ์การใช้งาน การจัดการไฟล์และไดเรกทอรี การตั้งค่าเครือข่ายและบริการพื้นฐาน', 'Study and practice of Linux operating system installation, user and permission administration, file and directory management, network configuration, and basic services.'),
(3, '030523111', 'ระบบฐานข้อมูล', 'DATABASE SYSTEMS', '2', 2568, '3(2-2-5)', 'ศึกษาสถาปัตยกรรมระบบฐานข้อมูล ตัวแบบข้อมูลเชิงสัมพันธ์ การออกแบบฐานข้อมูลด้วย E-R Model การทำนอร์มัลไลเซชัน และการใช้ภาษา SQL เพื่อจัดการข้อมูล', 'Study of database system architecture, relational data models, database design using E-R Model, normalization, and the use of SQL for data management.'),
(4, '030523201', 'ความมั่นคงปลอดภัยเครือข่ายและวิทยาการรหัสลับ', 'NETWORK SECURE & CRYPTO', '1', 2568, '3(3-0-6)', 'ศึกษาหลักการรักษาความปลอดภัยของระบบเครือข่าย ภัยคุกคามและช่องโหว่ วิทยาการรหัสลับเบื้องต้น การเข้ารหัสข้อมูล การจัดการกุญแจเข้ารหัส และโปรโตคอลความปลอดภัย', 'Study of network security principles, threats and vulnerabilities, introduction to cryptography, data encryption, key management, and security protocols.'),
(5, '030523301', 'วิศวกรรมซอฟต์แวร์', 'SOFTWARE ENGINEERING', '1', 2567, '3(3-0-6)', 'ศึกษาวงจรการพัฒนาซอฟต์แวร์ การวิเคราะห์และออกแบบระบบ การบริหารโครงการซอฟต์แวร์ การทดสอบและประกันคุณภาพซอฟต์แวร์ และการบำรุงรักษาระบบ', 'Study of software development life cycles, system analysis and design, software project management, software testing and quality assurance, and system maintenance.'),
(6, '030523302', 'การพัฒนาเว็บแอปพลิเคชัน', 'WEB APPLICATION DEVELOPMENT', '3', 2567, '3(2-2-5)', 'ศึกษาหลักการและฝึกปฏิบัติการพัฒนาเว็บแอปพลิเคชัน การทำงานฝั่งไคลเอนต์และเซิร์ฟเวอร์ การเชื่อมต่อฐานข้อมูลบนเว็บ และการประยุกต์ใช้เฟรมเวิร์กที่ทันสมัย', 'Study of principles and practice in web application development, client-side and server-side programming, web database connectivity, and application of modern web frameworks.');

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `mappings`
--

CREATE TABLE `mappings` (
  `id` int(11) NOT NULL,
  `clo_id` int(11) DEFAULT NULL,
  `map_type` varchar(10) DEFAULT NULL,
  `target_num` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `mappings`
--

INSERT INTO `mappings` (`id`, `clo_id`, `map_type`, `target_num`) VALUES
(1, 1, 'PLO', 1),
(2, 1, 'YLO', 1),
(3, 2, 'PLO', 2),
(4, 2, 'YLO', 2),
(5, 3, 'PLO', 2),
(6, 3, 'PLO', 5),
(7, 3, 'YLO', 4),
(8, 4, 'PLO', 4),
(9, 4, 'PLO', 8),
(10, 4, 'YLO', 6),
(11, 5, 'PLO', 1),
(12, 6, 'PLO', 1),
(13, 6, 'PLO', 3),
(14, 6, 'YLO', 2),
(15, 6, 'YLO', 5),
(16, 7, 'PLO', 3),
(17, 8, 'PLO', 3),
(18, 8, 'YLO', 6),
(19, 9, 'PLO', 6),
(20, 9, 'YLO', 3),
(21, 10, 'PLO', 1),
(22, 10, 'PLO', 2),
(23, 10, 'YLO', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role` varchar(20) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `name` varchar(255) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `role`, `created_at`, `name`) VALUES
(1, 'admin', '1234', 'admin@studentport.com', 'admin', '2026-04-07 04:41:24', 'แอดมิน (แก้ไขได้)'),
(2, 'viewer', '$2b$12$UA/lRl.jYydQ4GQxAtUY7.BNg462sxlOs8zxihGBfP2aN4ylM2Uhy', 'viewer@studentport.com', 'viewer', '2026-04-07 04:41:24', 'viewer'),
(3, 'psp', '1234', 'psp@student.local', 'viewer', '2026-04-07 12:43:32', 'คุณ psp (ดูได้อย่างเดียว)');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clos`
--
ALTER TABLE `clos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_items_id` (`id`),
  ADD KEY `ix_items_title` (`title`);

--
-- Indexes for table `mappings`
--
ALTER TABLE `mappings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_users_email` (`email`),
  ADD UNIQUE KEY `ix_users_username` (`username`),
  ADD KEY `ix_users_id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clos`
--
ALTER TABLE `clos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `mappings`
--
ALTER TABLE `mappings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
