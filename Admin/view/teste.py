from Admin.view.PlanosView import *
from Admin.view.AlunosView import *
from Admin.view.MatriculaView import *

from datetime import datetime


MatriculaView.inserir_matricula(1, 5, datetime.now().strftime('%d/%m/%Y'))