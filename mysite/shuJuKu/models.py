# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bus(models.Model):
    buscode = models.AutoField(db_column='busCode', primary_key=True)  # Field name made lowercase.
    buslicense = models.CharField(db_column='busLicense', max_length=20)  # Field name made lowercase.
    bustype = models.CharField(db_column='busType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    busstatus = models.CharField(db_column='busStatus', max_length=2, blank=True, null=True)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bus'


class Line(models.Model):
    linecode = models.AutoField(db_column='lineCode', primary_key=True)  # Field name made lowercase.
    linename = models.CharField(db_column='lineName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=2, blank=True, null=True)
    startlinetime = models.DateTimeField(db_column='startLineTime', blank=True, null=True)  # Field name made lowercase.
    direction = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'line'


class LineStationRef(models.Model):
    linecode = models.ForeignKey(Line, models.DO_NOTHING, db_column='lineCode', blank=True, null=True)  # Field name made lowercase.
    stationcode = models.ForeignKey('Station', models.DO_NOTHING, db_column='stationCode', blank=True, null=True)  # Field name made lowercase.
    stationorder = models.IntegerField(db_column='stationOrder', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'line_station_ref'


class Permission(models.Model):
    permissioncode = models.AutoField(db_column='permissionCode', primary_key=True)  # Field name made lowercase.
    permissionname = models.CharField(db_column='permissionName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    permissiondescribe = models.CharField(db_column='permissionDescribe', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'permission'


class Role(models.Model):
    rolecode = models.AutoField(db_column='roleCode', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='roleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    roledescribe = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'role'


class RolePermissionRef(models.Model):
    relationcode = models.AutoField(db_column='relationCode', primary_key=True)  # Field name made lowercase.
    rolecode = models.ForeignKey(Role, models.DO_NOTHING, db_column='roleCode', blank=True, null=True)  # Field name made lowercase.
    permissioncode = models.ForeignKey(Permission, models.DO_NOTHING, db_column='permissionCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'role_permission_ref'


class Scheduling(models.Model):
    code = models.AutoField(primary_key=True)
    linecode = models.ForeignKey(Line, models.DO_NOTHING, db_column='lineCode', blank=True, null=True)  # Field name made lowercase.
    tcnumber = models.CharField(db_column='tcNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tctime = models.CharField(db_column='tcTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usercode = models.ForeignKey('Sysuser', models.DO_NOTHING, db_column='userCode', blank=True, null=True)  # Field name made lowercase.
    startstation = models.ForeignKey('Station', models.DO_NOTHING, db_column='startStation', blank=True, null=True)  # Field name made lowercase.
    endstation = models.ForeignKey('Station', models.DO_NOTHING, db_column='endStation', blank=True, null=True,related_name='endStation')  # Field name made lowercase.
    buslicense = models.ForeignKey(Bus, models.DO_NOTHING, db_column='busLicense', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'scheduling'


class Station(models.Model):
    stationcode = models.AutoField(db_column='stationCode', primary_key=True)  # Field name made lowercase.
    stationname = models.CharField(db_column='stationName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'station'


class Sysuser(models.Model):
    code = models.AutoField(primary_key=True)
    loginname = models.CharField(db_column='loginName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    idcard = models.CharField(db_column='idCard', max_length=25, blank=True, null=True)  # Field name made lowercase.
    role = models.ForeignKey(Role,models.DO_NOTHING, db_column='role', blank=True, null=True)
    driving = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sysuser'
