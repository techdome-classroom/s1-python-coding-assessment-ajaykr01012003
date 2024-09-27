def decode_message(s: str, p: str) -> bool:

    def match_helper(m_idx: int, p_idx: int) -> bool:
  
        if p_idx == len(p):
      
            return m_idx == len(s)

        if p[p_idx] == '*':
            
            return match_helper(m_idx, p_idx + 1) or (m_idx < len(s) and match_helper(m_idx + 1, p_idx))

   
        if m_idx < len(s) and (p[p_idx] == '?' or p[p_idx] == s[m_idx]):
            return match_helper(m_idx + 1, p_idx + 1)

   
        return False

    return match_helper(0, 0)
