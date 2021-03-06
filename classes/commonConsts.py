from classes.appFunctions import hexToTuple

def getProbsOnCosts(*costs):
	"""
	Принимает массив цен на артефакты, возвращает массив вероятностей
	их появления с учетом того, что цена обратно пропорциональна вероятности
	появления."""
	devider = 1
	for i in range(1, len(costs)):
		devider += costs[0] / costs[i]
	probs = [round(1 / devider, 3)]
	for i in range(1, len(costs)):
		probs.append(round(probs[0] * costs[0] / costs[i], 3))
	return probs

#параметры артефактов
artefactSize = 10#радиус артефакта при отрисовке
artefactQuantitiy = 10#количество артефактов на поле
artefactsTypes = {}#словарь с типами артефактов
artefactsTypes['redball'] = {'color': hexToTuple('EC0000'), 'price':5000, 'prob': 0.125}
artefactsTypes['blueball'] = {'color': hexToTuple('0246C3'), 'price':2500, 'prob': 0.25}
artefactsTypes['grayball'] = {'color': hexToTuple('D8C6C6'), 'price':1000, 'prob': 0.625}

artTypesTuple = tuple(x for x in artefactsTypes)
artProbsTuple = tuple(artefactsTypes[x]['prob'] for x in artefactsTypes)


#параметры экрана
WIDTHSCREEN = 1024
HEIGHTSCREEN = 700