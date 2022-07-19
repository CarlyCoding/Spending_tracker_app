from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models import merchant
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.type_repository as type_repository

merchant_blueprint = Merchant("merchant", __name__)


# GET
# CREATE
# SHOW
# EDIT
# UPDATE 
# DELETE 