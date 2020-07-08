class extractor():

    def response_extract(self, msg):
        resultdict = {}
        for key1, value1 in msg.items():
            if key1 == 'output':
                for key2, value2 in value1.items():
                    if key2 == 'generic':
                        for i in value2:
                            for key4, value4 in i.items():
                                if key4 == 'text':
                                    if 'response' in resultdict.keys():
                                        resultdict['response'].append(value4)
                                    else:
                                        resultdict['response'] = [value4]
        return resultdict

    def context_variable_extractor(self, msg):

        result = {}
        for key1, value1 in msg.items():
            if key1 == 'context':
                for key2, value2 in value1.items():
                    if key2 == 'skills':
                        for key3, value3 in value2.items():
                            for key4, value4 in value3.items():
                                for key5, value5 in value4.items():
                                    result[key5] = value5

        return result
