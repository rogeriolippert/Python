'''
# A função aiter(async_iterable) não é uma função padrão do Python. 
# Parece que você está se referindo ao uso do método __aiter__ que é usado em coroutines assíncronas 
# para obter um iterador assíncrono. Em Python, objetos assíncronos que suportam a criação de iteradores assíncronos 
# podem implementar o método especial __aiter__. Este método é chamado quando você usa aiter() em um objeto assíncrono.
#
# Aqui está um exemplo simples: #Exemplo de uso 
#
# Neste exemplo, a classe AsyncCounter implementa os métodos __aiter__ e __anext__. O método __aiter__ é chamado 
# quando você chama aiter() no objeto assíncrono, e o método __anext__ 
# é chamado a cada iteração do loop assíncrono (async for).
#
# A função aiter(async_iterable) pode ser usada para obter um iterador assíncrono a partir de um objeto assíncrono
# que implementa __aiter__. Em resumo, aiter é um método que permite a criação de iteradores assíncronos em Python.
'''
class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit

    async def __aiter__(self):
        self.current = 0
        return self

    async def __anext__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopAsyncIteration

# Exemplo de uso
async def main():
    async_counter = AsyncCounter(5)
    
    async for value in async_counter:
        print(value)

# Executando a coroutine
import asyncio
asyncio.run(main())
