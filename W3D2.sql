-- Es.1
select NomeCantante
from CANTANTE as c join ESECUZIONE as e on
c.CodiceReg=e.CodiceReg
join AUTORE as a on e.TitoloCanz=a.TitoloCanzone
where Nome=NomeCantante and Nome like ‘d%’

-- Es.2
select TitoloAlbum
from DISCO as d join CONTIENE as c on d.NroSerie=c.NroSerieDisco
join ESECUZIONE as e on c.CodiceReg=e.CodiceReg
where e.anno is NULL 

--Es.3
select distinct NomeCantante
from CANTANTE
where NomeCantante not in
( select C1.NomeCantante
 from CANTANTE as C1
 where CodiceReg not in
( select CodiceReg
 from CANTANTE S2
 where C2.NomeCantante <> C1.NomeCantante ) )

--Es.4
select NomeCantante
from CANTANTE
where NomeCantante not in
( select S1.NomeCantante
 from CANTANTE as S1 join ESECUZIONE on CodiceReg=S1.CodiceReg
 join CANTANTE as S2 on CodiceReg=S2.CodiceReg )
 where S1.NomeCantante<> S2.NomeCantante)
