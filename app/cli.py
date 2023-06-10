import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Hotel, Customer, Review

# Create the SQLAlchemy engine and session
engine = create_engine('sqlite:///hotels.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
def create_tables():
    """Create the database tables"""
    Base.metadata.create_all(engine)
    click.echo("Tables created successfully.")

@cli.command()
def migrate():
    """Run database migrations using Alembic"""
    from alembic.config import Config
    from alembic import command

    alembic_cfg = Config("app/alembic.ini")
    command.upgrade(alembic_cfg, "head")
    click.echo("Migrations completed successfully.")

@cli.command()
@click.argument('name')
@click.argument('price', type=int)
def add_hotel(name, price):
    """Add a new hotel"""
    hotel = Hotel(name=name, price=price)
    session.add(hotel)
    session.commit()
    click.echo(f"Hotel '{name}' added successfully.")

@cli.command()
@click.argument('first_name')
@click.argument('last_name')
def add_customer(first_name, last_name):
    """Add a new customer"""
    customer = Customer(first_name=first_name, last_name=last_name)
    session.add(customer)
    session.commit()
    click.echo(f"Customer '{first_name} {last_name}' added successfully.")

@cli.command()
@click.argument('hotel_id', type=int)
@click.argument('customer_id', type=int)
@click.argument('rating', type=int)
def add_review(hotel_id, customer_id, rating):
    """Add a new review"""
    hotel = session.query(Hotel).get(hotel_id)
    customer = session.query(Customer).get(customer_id)
    
    if hotel and customer:
        review = Review(star_rating=rating, hotel=hotel, customer=customer)
        session.add(review)
        session.commit()
        click.echo("Review added successfully.")
    else:
        click.echo("Invalid hotel or customer ID. Please try again.")

if __name__ == '__main__':
    cli()
