
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEQNEQleftGTELTEGTLTCOM DIVIDA DOIS_PONTOS ENQUANTO ENTAO EQ FACA FIM GT GTE LT LTE MOSTRE MULTIPLIQUE NEQ NUM PONTO POR REPITA SE SENAO SER SOME SUBTRAIA VAR VEZESprograma : cmdscmds : cmd cmds\n            | cmdcmd : atribuicao\n           | impressao\n           | operacao\n           | repeticao\n           | multiplique\n           | divisao\n           | subtracao\n           | se\n           | repeticao_enquantoatribuicao : FACA VAR SER NUM PONTO\n                  | FACA VAR SER VAR PONTO\n                  | FACA VAR SER expressao PONTOimpressao : MOSTRE VAR PONTO\n                 | MOSTRE NUM PONTOoperacao : SOME VAR COM VAR PONTO\n                | SOME VAR COM NUM PONTOmultiplique : MULTIPLIQUE VAR POR VAR PONTO\n           | MULTIPLIQUE VAR POR NUM PONTOdivisao : DIVIDA VAR POR NUM PONTO\n           | DIVIDA VAR POR VAR PONTOsubtracao : SUBTRAIA VAR POR NUM PONTO\n           | SUBTRAIA VAR POR VAR PONTOrepeticao : REPITA NUM VEZES DOIS_PONTOS cmds FIMrepeticao_enquanto : REPITA ENQUANTO expressao DOIS_PONTOS cmds FIMexpressao : expressao EQ expressao\n                | expressao NEQ expressao\n                | expressao GTE expressao\n                | expressao LTE expressao\n                | expressao GT expressao\n                | expressao LT expressaoexpressao : VAR\n                | NUMse : SE expressao ENTAO cmds FIM\n          | SE expressao ENTAO cmds SENAO cmds FIM\n          | SE expressao ENTAO cmds FIM PONTO\n          | SE expressao ENTAO cmds SENAO cmds FIM PONTO'
    
_lr_action_items = {'FACA':([0,3,4,5,6,7,8,9,10,11,12,35,36,43,55,56,70,71,72,73,74,77,78,79,80,81,82,83,84,85,86,87,89,90,],[13,13,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,13,13,13,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,13,-26,-27,-38,-37,-39,]),'MOSTRE':([0,3,4,5,6,7,8,9,10,11,12,35,36,43,55,56,70,71,72,73,74,77,78,79,80,81,82,83,84,85,86,87,89,90,],[14,14,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,14,14,14,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,14,-26,-27,-38,-37,-39,]),'SOME':([0,3,4,5,6,7,8,9,10,11,12,35,36,43,55,56,70,71,72,73,74,77,78,79,80,81,82,83,84,85,86,87,89,90,],[15,15,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,15,15,15,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,15,-26,-27,-38,-37,-39,]),'REPITA':([0,3,4,5,6,7,8,9,10,11,12,35,36,43,55,56,70,71,72,73,74,77,78,79,80,81,82,83,84,85,86,87,89,90,],[16,16,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,16,16,16,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,16,-26,-27,-38,-37,-39,]),'MULTIPLIQUE':([0,3,4,5,6,7,8,9,10,11,12,35,36,43,55,56,70,71,72,73,74,77,78,79,80,81,82,83,84,85,86,87,89,90,],[17,17,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,17,17,17,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,17,-26,-27,-38,-37,-39,]),'DIVIDA':([0,3,4,5,6,7,8,9,10,11,12,35,36,43,55,56,70,71,72,73,74,77,78,79,80,81,82,83,84,85,86,87,89,90,],[18,18,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,18,18,18,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,18,-26,-27,-38,-37,-39,]),'SUBTRAIA':([0,3,4,5,6,7,8,9,10,11,12,35,36,43,55,56,70,71,72,73,74,77,78,79,80,81,82,83,84,85,86,87,89,90,],[19,19,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,19,19,19,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,19,-26,-27,-38,-37,-39,]),'SE':([0,3,4,5,6,7,8,9,10,11,12,35,36,43,55,56,70,71,72,73,74,77,78,79,80,81,82,83,84,85,86,87,89,90,],[20,20,-4,-5,-6,-7,-8,-9,-10,-11,-12,-16,-17,20,20,20,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,20,-26,-27,-38,-37,-39,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,21,35,36,70,71,72,73,74,77,78,79,80,81,82,83,85,86,87,89,90,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-16,-17,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,-26,-27,-38,-37,-39,]),'FIM':([3,4,5,6,7,8,9,10,11,12,21,35,36,63,70,71,72,73,74,75,76,77,78,79,80,81,82,83,85,86,87,88,89,90,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-16,-17,83,-14,-13,-15,-18,-19,85,86,-20,-21,-23,-22,-25,-24,-36,-26,-27,-38,89,-37,-39,]),'SENAO':([3,4,5,6,7,8,9,10,11,12,21,35,36,63,70,71,72,73,74,77,78,79,80,81,82,83,85,86,87,89,90,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-16,-17,84,-14,-13,-15,-18,-19,-20,-21,-23,-22,-25,-24,-36,-26,-27,-38,-37,-39,]),'VAR':([13,14,15,17,18,19,20,27,34,37,40,41,42,44,45,46,47,48,49,],[22,23,25,28,29,30,32,32,50,53,57,59,61,32,32,32,32,32,32,]),'NUM':([14,16,20,27,34,37,40,41,42,44,45,46,47,48,49,],[24,26,33,33,51,54,58,60,62,33,33,33,33,33,33,]),'ENQUANTO':([16,],[27,]),'SER':([22,],[34,]),'PONTO':([23,24,32,33,50,51,52,53,54,57,58,59,60,61,62,64,65,66,67,68,69,83,89,],[35,36,-34,-35,70,71,72,73,74,77,78,79,80,81,82,-28,-29,-30,-31,-32,-33,87,90,]),'COM':([25,],[37,]),'VEZES':([26,],[38,]),'POR':([28,29,30,],[40,41,42,]),'ENTAO':([31,32,33,64,65,66,67,68,69,],[43,-34,-35,-28,-29,-30,-31,-32,-33,]),'EQ':([31,32,33,39,50,51,52,64,65,66,67,68,69,],[44,-34,-35,44,-34,-35,44,-28,-29,-30,-31,-32,-33,]),'NEQ':([31,32,33,39,50,51,52,64,65,66,67,68,69,],[45,-34,-35,45,-34,-35,45,-28,-29,-30,-31,-32,-33,]),'GTE':([31,32,33,39,50,51,52,64,65,66,67,68,69,],[46,-34,-35,46,-34,-35,46,46,46,-30,-31,-32,-33,]),'LTE':([31,32,33,39,50,51,52,64,65,66,67,68,69,],[47,-34,-35,47,-34,-35,47,47,47,-30,-31,-32,-33,]),'GT':([31,32,33,39,50,51,52,64,65,66,67,68,69,],[48,-34,-35,48,-34,-35,48,48,48,-30,-31,-32,-33,]),'LT':([31,32,33,39,50,51,52,64,65,66,67,68,69,],[49,-34,-35,49,-34,-35,49,49,49,-30,-31,-32,-33,]),'DOIS_PONTOS':([32,33,38,39,64,65,66,67,68,69,],[-34,-35,55,56,-28,-29,-30,-31,-32,-33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'cmds':([0,3,43,55,56,84,],[2,21,63,75,76,88,]),'cmd':([0,3,43,55,56,84,],[3,3,3,3,3,3,]),'atribuicao':([0,3,43,55,56,84,],[4,4,4,4,4,4,]),'impressao':([0,3,43,55,56,84,],[5,5,5,5,5,5,]),'operacao':([0,3,43,55,56,84,],[6,6,6,6,6,6,]),'repeticao':([0,3,43,55,56,84,],[7,7,7,7,7,7,]),'multiplique':([0,3,43,55,56,84,],[8,8,8,8,8,8,]),'divisao':([0,3,43,55,56,84,],[9,9,9,9,9,9,]),'subtracao':([0,3,43,55,56,84,],[10,10,10,10,10,10,]),'se':([0,3,43,55,56,84,],[11,11,11,11,11,11,]),'repeticao_enquanto':([0,3,43,55,56,84,],[12,12,12,12,12,12,]),'expressao':([20,27,34,44,45,46,47,48,49,],[31,39,52,64,65,66,67,68,69,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> cmds','programa',1,'p_programa','parser.py',13),
  ('cmds -> cmd cmds','cmds',2,'p_cmds','parser.py',18),
  ('cmds -> cmd','cmds',1,'p_cmds','parser.py',19),
  ('cmd -> atribuicao','cmd',1,'p_cmd','parser.py',26),
  ('cmd -> impressao','cmd',1,'p_cmd','parser.py',27),
  ('cmd -> operacao','cmd',1,'p_cmd','parser.py',28),
  ('cmd -> repeticao','cmd',1,'p_cmd','parser.py',29),
  ('cmd -> multiplique','cmd',1,'p_cmd','parser.py',30),
  ('cmd -> divisao','cmd',1,'p_cmd','parser.py',31),
  ('cmd -> subtracao','cmd',1,'p_cmd','parser.py',32),
  ('cmd -> se','cmd',1,'p_cmd','parser.py',33),
  ('cmd -> repeticao_enquanto','cmd',1,'p_cmd','parser.py',34),
  ('atribuicao -> FACA VAR SER NUM PONTO','atribuicao',5,'p_atribuicao','parser.py',38),
  ('atribuicao -> FACA VAR SER VAR PONTO','atribuicao',5,'p_atribuicao','parser.py',39),
  ('atribuicao -> FACA VAR SER expressao PONTO','atribuicao',5,'p_atribuicao','parser.py',40),
  ('impressao -> MOSTRE VAR PONTO','impressao',3,'p_impressao','parser.py',49),
  ('impressao -> MOSTRE NUM PONTO','impressao',3,'p_impressao','parser.py',50),
  ('operacao -> SOME VAR COM VAR PONTO','operacao',5,'p_operacao','parser.py',54),
  ('operacao -> SOME VAR COM NUM PONTO','operacao',5,'p_operacao','parser.py',55),
  ('multiplique -> MULTIPLIQUE VAR POR VAR PONTO','multiplique',5,'p_multiplique','parser.py',59),
  ('multiplique -> MULTIPLIQUE VAR POR NUM PONTO','multiplique',5,'p_multiplique','parser.py',60),
  ('divisao -> DIVIDA VAR POR NUM PONTO','divisao',5,'p_divisao','parser.py',64),
  ('divisao -> DIVIDA VAR POR VAR PONTO','divisao',5,'p_divisao','parser.py',65),
  ('subtracao -> SUBTRAIA VAR POR NUM PONTO','subtracao',5,'p_subtracao','parser.py',69),
  ('subtracao -> SUBTRAIA VAR POR VAR PONTO','subtracao',5,'p_subtracao','parser.py',70),
  ('repeticao -> REPITA NUM VEZES DOIS_PONTOS cmds FIM','repeticao',6,'p_repeticao','parser.py',74),
  ('repeticao_enquanto -> REPITA ENQUANTO expressao DOIS_PONTOS cmds FIM','repeticao_enquanto',6,'p_repeticao_enquanto','parser.py',79),
  ('expressao -> expressao EQ expressao','expressao',3,'p_expressao_binaria','parser.py',84),
  ('expressao -> expressao NEQ expressao','expressao',3,'p_expressao_binaria','parser.py',85),
  ('expressao -> expressao GTE expressao','expressao',3,'p_expressao_binaria','parser.py',86),
  ('expressao -> expressao LTE expressao','expressao',3,'p_expressao_binaria','parser.py',87),
  ('expressao -> expressao GT expressao','expressao',3,'p_expressao_binaria','parser.py',88),
  ('expressao -> expressao LT expressao','expressao',3,'p_expressao_binaria','parser.py',89),
  ('expressao -> VAR','expressao',1,'p_expressao_basica','parser.py',93),
  ('expressao -> NUM','expressao',1,'p_expressao_basica','parser.py',94),
  ('se -> SE expressao ENTAO cmds FIM','se',5,'p_se','parser.py',98),
  ('se -> SE expressao ENTAO cmds SENAO cmds FIM','se',7,'p_se','parser.py',99),
  ('se -> SE expressao ENTAO cmds FIM PONTO','se',6,'p_se','parser.py',100),
  ('se -> SE expressao ENTAO cmds SENAO cmds FIM PONTO','se',8,'p_se','parser.py',101),
]
