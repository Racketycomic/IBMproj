class extractor():


    def response_extract(self, msg):
        resultdict = {}
        arr = msg['output']['generic']
        for i in arr:
            for key4, value4 in i.items():
                if key4 == 'text':
                    if 'response' in resultdict.keys():
                        if len(value4) != 0:
                            resultdict['response'].append(value4)
                    else:
                        if len(value4) != 0:
                            resultdict['response'] = [value4]
        return resultdict

    def context_variable_extractor(self, msg):
        result = {}
        result = msg['context']['skills']['main skill']['user_defined']
        return result

    def split_and_compile(self, msg_arr):

        result = msg_arr.split('|')
        return result
