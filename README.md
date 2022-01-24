# Booking System

## Modelo del domino inicial:

![booking-DM](http://www.plantuml.com/plantuml/png/PL9DRzmW4BtpAr1E-P0ZzGzKiGrjKNRPhSrMxSaYQxonQY22SQLLbV_UDIPUhDuUR-OnysRcoODqCEe1AJDgN5ZxkpUd6YIC7lz563_WFUM4yQyppXa9WD0D5PIWTtGSfFUO6L3kZno811Lq6GumV3-XAwLC6ua7x5-j0tnIm4Vzejok8_BiR-z2BFroIYcjwOR-2BTfu6xf8BQU5Zyw9K65QajQPQsEEJMuIM12QVGU9X3Yuloceldwudn3PykxGn6XgDW-mk-7d4H0AG_e-Q9954qYf3zfUH3i1stg0nCJbyKPc3Y0GhK-qDrW9U0trn-lpPUZ1wkLMnleUkU1IwrISf3_Swtfm_F5sa59Wq-Zyl1XV2_FMXdOAdYrRNHVvlMtkEw2YQRCApBp5INfUxihsCNeFl-rfLpCJZUq5DMEix8fSlxSY2hdzHTQBLvYlTbAT2kr7GrS5zZEcqCVkysop-iJNIBtMROwc5GIThhAlFdq-7X_iumJnLxI_z4aYkhv8jAizRJGapBjg8T_)



### Endpoints:
Se tienen los siguientes endpoints:
* **/api/v1/customers/**: Este endpoint se encarga de las operaciones CRUD sobre los clientes de la aplicación.
~~~
{
    "id": <BigInteger>,
    "first_name": <String>,
    "last_name": <String>,
    "dni": <String>,
    "guest": <Boolean>
}
~~~
* **/api/v1/rooms/**: Este endpoint se encarga de las operaciones CRUD sobre las habitaciónes disponibles en la aplicación.
~~~
{
    "id": <BigInteger>,
    "number": <String>,
    "room_type": <String>
}
~~~
* **/api/v1/bookings/**: Este endpoint se encarga de las operaciones CRUD sobre las reservas mediante la aplicación.
~~~
{
    "id": <BigInteger>,
    "booking_date_id": <BigInteger>,
    "room_id": <BigInteger>,
    "customers": <Array>,
    "created_date_time": <String>,
    "status": <String>
}
~~~
* **/api/v1/bookings/{id}/payments/**: Este endpoint se encarga de las operaciones CRUD sobre los pagos de cada reserva.
~~~
{
    "id": <BigInteger>,
    "payment_method": <String>,
    "amount": <Float>
}
~~~
