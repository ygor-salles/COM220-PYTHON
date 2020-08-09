import Aluno as al 
import Curso as cr 
import Grade as gr 
import Disciplina as dic 
import Historico as hist 

print()
aluno1 = al.Aluno('2017014382', 'Ygor')
aluno1.setCurso('SIN')
aluno2 = al.Aluno('2017014382', 'Salles')
aluno2.setCurso('CCO')
print(aluno1)
print()

disc1 = dic.Disciplina('MAT0013', 'Probabilidade', 64)
disc2 = dic.Disciplina('COM220', 'POO', 64)
print(disc1)
print()

listaDisc = [disc1, disc2]
gradeSin2018 = gr.Grade(2018, listaDisc)
gradeSin2018.setCurso('SIN')
gradeSin2018.mostra()
print()

listaAluno = [aluno1]
cursoSin = cr.Curso('SIN', listaAluno, gradeSin2018)
cursoSin.mostra()
print()

historico = hist.Historico(listaDisc, aluno1, gradeSin2018)
historico.mostra()

