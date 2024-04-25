class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = "the sky is blue"
        #for loop the string
        #nstring = ""
        
        word_array = []
        n_string = ""
        for lett in s:
            if lett == " " and len(n_string) > 0:
                word_array.append(n_string)
                n_string = ""
                continue
            if lett== " " and len(n_string) == 0:
                continue
            else:
                n_string += lett
        if n_string:
            word_array.append(n_string)
        print ("word_array", word_array)
        
        final_string = ""
        while word_array:
            final_word = word_array.pop()
            final_string += final_word + " "
        
        final_string = final_string [:-1]
        
        return final_string
        
        
                
            