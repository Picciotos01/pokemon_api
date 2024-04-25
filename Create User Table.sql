use pokedex;

--
-- Table structure for table `user`
--

create table `user` (
	`id` int auto_increment PRIMARY KEY,
    `pseudo` varchar(50) NOT NULL,
    `password` varchar(50) NOT NULL,
    `role` varchar(10) default 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `user` (`pseudo`, `password`, `role`) VALUES
('administrator', '123', 'admin');


--
-- Table structure for table `bag`
--

create table `bag` (
	`user_id` int NOT NULL,
    `pokemon_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;