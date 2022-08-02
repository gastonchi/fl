1- SELECT * FROM Estudiante WHERE Carrera='informática';
2- SELECT * FROM Estudiante WHERE Nombre LIKE 'G%';
3- SELECT * FROM Libros L LEFT JOIN Prestamo P on P.idLibro = L.IdLibro LEFT JOIN Estudiante E ON E.idLector = P.idLector WHERE E.Nombre='Raul Valdez Alanes';
