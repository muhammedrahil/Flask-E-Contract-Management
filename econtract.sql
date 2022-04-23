/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - econtractor
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`econtractor` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `econtractor`;

/*Table structure for table `applyjob` */

DROP TABLE IF EXISTS `applyjob`;

CREATE TABLE `applyjob` (
  `applyid` int(11) NOT NULL AUTO_INCREMENT,
  `vacancyid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `resume` varchar(900) DEFAULT NULL,
  PRIMARY KEY (`applyid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `applyjob` */

insert  into `applyjob`(`applyid`,`vacancyid`,`userid`,`date`,`status`,`resume`) values 
(1,1,4,'2022-03-17','accept','ec.png'),
(2,3,4,'2022-03-17','pending','login.css'),
(3,4,4,'2022-04-15','pending','SS - MODULE 4--converted.pdf'),
(4,3,4,'2022-04-15','pending','SS_Module_5_--converted.pdf');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chatid` int(11) NOT NULL AUTO_INCREMENT,
  `fromid` int(11) DEFAULT NULL,
  `toid` int(11) DEFAULT NULL,
  `massage` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chatid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaintid` int(11) NOT NULL AUTO_INCREMENT,
  `compalaint` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `replay` varchar(50) DEFAULT NULL,
  `conid` int(10) DEFAULT NULL,
  `rid` int(10) DEFAULT NULL,
  PRIMARY KEY (`complaintid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaintid`,`compalaint`,`date`,`userid`,`replay`,`conid`,`rid`) values 
(1,'no','2022-03-24',4,'sorry',2,1),
(2,'not working','2022-04-15',4,'pending',2,2);

/*Table structure for table `contractor` */

DROP TABLE IF EXISTS `contractor`;

CREATE TABLE `contractor` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `sevice` varchar(50) DEFAULT NULL,
  `loginid` int(11) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `contractor` */

insert  into `contractor`(`cid`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`phone`,`sevice`,`loginid`) values 
(1,'muhammed','rahil','Male','malapuram','areecode',673639,7592978136,'Web Application Developer',2),
(2,'lalu','llal','Male','Areecode','dmks',1223,1233144,'digital Markating',5);

/*Table structure for table `features` */

DROP TABLE IF EXISTS `features`;

CREATE TABLE `features` (
  `featureid` int(11) NOT NULL AUTO_INCREMENT,
  `contractid` int(11) DEFAULT NULL,
  `skills` varchar(50) DEFAULT NULL,
  `experiance` varchar(50) DEFAULT NULL,
  `work` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`featureid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `features` */

insert  into `features`(`featureid`,`contractid`,`skills`,`experiance`,`work`) values 
(1,2,'digital marketing','2 year','login.css'),
(6,5,'jsdbhs','123','SS - MODULE 4--converted.pdf');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedid` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(50) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `cid` int(50) DEFAULT NULL,
  PRIMARY KEY (`feedid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedid`,`feedback`,`userid`,`date`,`cid`) values 
(1,'good',4,'2022-03-24',2);

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `locationid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`locationid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `location` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`usertype`) values 
(1,'admin','123','admin'),
(2,'contractor','123','contractor'),
(3,'asd','123','contractor'),
(4,'user','123','user'),
(5,'as','123','contractor');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `requestid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `conid` int(11) DEFAULT NULL,
  `work` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`requestid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`requestid`,`userid`,`conid`,`work`,`date`,`status`) values 
(1,4,2,'econ.jpg','2022-03-17','accept'),
(2,4,2,'ec.png','2022-03-20','accept'),
(4,4,2,'SS_Module_5_--converted.pdf','2022-04-14','pending'),
(5,4,5,'SS_MODULE_2--converted.pdf','2022-04-14','accept');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `phonenumber` bigint(20) DEFAULT NULL,
  `loginid` int(11) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`userid`,`fname`,`lname`,`place`,`post`,`pin`,`phonenumber`,`loginid`) values 
(1,'muhammed','rahil','Areecode','areecode',673639,7592978136,4);

/*Table structure for table `vaccancy` */

DROP TABLE IF EXISTS `vaccancy`;

CREATE TABLE `vaccancy` (
  `vaccid` int(11) NOT NULL AUTO_INCREMENT,
  `job` varchar(50) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  `contractid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `vacancy` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`vaccid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `vaccancy` */

insert  into `vaccancy`(`vaccid`,`job`,`details`,`contractid`,`date`,`vacancy`) values 
(1,'developer','degree must',2,'2022-03-17','10'),
(2,'developer','degree must',2,'2022-03-17','10'),
(3,'shop worker','12000 month',2,'2022-03-17','2'),
(4,'computer','12th',5,'2022-04-15','12');

/*Table structure for table `workdeatails` */

DROP TABLE IF EXISTS `workdeatails`;

CREATE TABLE `workdeatails` (
  `wid` int(10) NOT NULL AUTO_INCREMENT,
  `workdeatails` varchar(1000) DEFAULT NULL,
  `file` varchar(1000) DEFAULT NULL,
  `rid` int(10) DEFAULT NULL,
  `cid` int(10) DEFAULT NULL,
  PRIMARY KEY (`wid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `workdeatails` */

insert  into `workdeatails`(`wid`,`workdeatails`,`file`,`rid`,`cid`) values 
(1,'nothing','ec.png',NULL,NULL),
(2,'geigeiwe','econtractReport2.docx.docx.docx',NULL,NULL),
(3,'344ertr','ja.jpg',NULL,NULL),
(4,'bbbabab','V_Sem_JavaScript__PHP-1.pdf',1,NULL),
(5,'asd','Cryptography__Network_Security_Module_5_1.pptx',5,5);

/*Table structure for table `works` */

DROP TABLE IF EXISTS `works`;

CREATE TABLE `works` (
  `workid` int(11) NOT NULL AUTO_INCREMENT,
  `loginid` int(11) DEFAULT NULL,
  `work` varchar(50) DEFAULT NULL,
  `document` varchar(50) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`workid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `works` */

insert  into `works`(`workid`,`loginid`,`work`,`document`,`status`) values 
(1,4,'construct','eco.png','your work accept'),
(2,4,'building construct','logo.png','pending'),
(3,4,'PLUMBER WORKS','Cryptography__Network_Security_Module_5.pptx','your work accept'),
(4,4,'education','SS_MODULE_2--converted.pdf','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
