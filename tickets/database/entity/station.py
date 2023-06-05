from django.db import models

class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)

    def __repr__(self) -> str:
        return f"Station(id={self.id}, name={self.name})"
    
    class Meta:
        db_table = 'station'