import streamlit as st
import time

if 'board' not in st.session_state:
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.turn = "X" 

def check_winner(b):
    lines = []
    for i in range(3):
        lines.append([b[i][0], b[i][1], b[i][2]])
        lines.append([b[0][i], b[1][i], b[2][i]])
    lines.append([b[0][0], b[1][1], b[2][2]])
    lines.append([b[0][2], b[1][1], b[2][0]])

    for line in lines:
        if line[0] == line[1] == line[2] != "":
            return line[0]
    if all(cell != "" for row in b for cell in row):
        return "Tie"
    return None

def get_bot_move():
    b = st.session_state.board
    win_paths = [
        [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]                        
    ]

    for path in win_paths:
        vals = [b[r][c] for r, c in path]
        if vals.count("O") == 2 and vals.count("") == 1:
            return path[vals.index("")]

    for path in win_paths:
        vals = [b[r][c] for r, c in path]
        if vals.count("X") == 2 and vals.count("") == 1:
            return path[vals.index("")]

    if b[1][1] == "":
        return (1, 1)

    for r in range(3):
        for c in range(3):
            if b[r][c] == "":
                return (r, c)
    return None

st.title("Tic Tac Toe")

winner = check_winner(st.session_state.board)

for r in range(3):
    cols = st.columns(3)
    for c in range(3):
        with cols[c]:
            label = st.session_state.board[r][c] or " "
            can_click = st.session_state.board[r][c] == "" and winner is None and st.session_state.turn == "X"
            if st.button(label, key=f"{r}-{c}", disabled=not can_click):
                st.session_state.board[r][c] = "X"
                st.session_state.turn = "O"
                st.rerun()
                
if winner:
    if winner == "Tie":
        st.info("It's a draw!")
    else:
        st.success(f"Player {winner} wins!")
elif st.session_state.turn == "O":
    with st.spinner("Bot is moving..."):
        time.sleep(0.5)
        move = get_bot_move()
        if move:
            st.session_state.board[move[0]][move[1]] = "O"
            st.session_state.turn = "X"
            st.rerun()

if st.button("Reset Game"):
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.turn = "X"
    st.rerun()