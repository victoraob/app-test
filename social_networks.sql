-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-01-2022 a las 00:19:02
-- Versión del servidor: 10.4.20-MariaDB
-- Versión de PHP: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `social_networks`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ages`
--

CREATE TABLE `ages` (
  `id_ages` int(11) NOT NULL,
  `name_ages` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ages`
--

INSERT INTO `ages` (`id_ages`, `name_ages`) VALUES
(1, '18-25'),
(2, '26-33'),
(3, '34-40'),
(4, '40+');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `networks`
--

CREATE TABLE `networks` (
  `id_net` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `networks`
--

INSERT INTO `networks` (`id_net`, `name`) VALUES
(1, 'facebook'),
(2, 'whatsapp'),
(3, 'twiter'),
(4, 'instagram'),
(5, 'TikTok');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participants`
--

CREATE TABLE `participants` (
  `id_participant` int(11) NOT NULL,
  `name_participant` varchar(255) NOT NULL,
  `email_participant` varchar(255) NOT NULL,
  `age_participant` int(11) NOT NULL,
  `gender_participant` int(11) NOT NULL,
  `favorite_network` int(11) NOT NULL,
  `time_facebook` int(11) NOT NULL,
  `time_whatsapp` int(11) NOT NULL,
  `time_twiter` int(11) NOT NULL,
  `time_instagram` int(11) NOT NULL,
  `time_tiktok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ages`
--
ALTER TABLE `ages`
  ADD PRIMARY KEY (`id_ages`);

--
-- Indices de la tabla `networks`
--
ALTER TABLE `networks`
  ADD PRIMARY KEY (`id_net`);

--
-- Indices de la tabla `participants`
--
ALTER TABLE `participants`
  ADD PRIMARY KEY (`id_participant`),
  ADD KEY `favorite_network` (`favorite_network`),
  ADD KEY `age_participant` (`age_participant`),
  ADD KEY `age_participant_2` (`age_participant`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ages`
--
ALTER TABLE `ages`
  MODIFY `id_ages` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `networks`
--
ALTER TABLE `networks`
  MODIFY `id_net` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `participants`
--
ALTER TABLE `participants`
  MODIFY `id_participant` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `participants`
--
ALTER TABLE `participants`
  ADD CONSTRAINT `participants_ibfk_1` FOREIGN KEY (`favorite_network`) REFERENCES `networks` (`id_net`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `participants_ibfk_2` FOREIGN KEY (`age_participant`) REFERENCES `ages` (`id_ages`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
