from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self,msg):
        raise NotImplemented('Implemente o metodo log')
    
    def Log_error(self,msg):
        return self._log(f'Error: {msg}')
    
    def Log_sucess(self,msg):
        return self._log(f'Sucess: {msg}')
        
    
class LogFileMixin(Log):
    def _log(self,msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'

        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self,msg):
        print(f'{msg} ({self.__class__.__name__})')
    

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.Log_error('')
    lp.Log_sucess('')
   

    lf = LogFileMixin()
    lf = LogFileMixin()
    lf.Log_error('')
    lf.Log_sucess('')
    