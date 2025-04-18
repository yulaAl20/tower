import streamlit as st

def render_game_board(state, n, pegs=3):
    """Render the Tower of Hanoi game board with Streamlit."""
    max_disk_width = 180  # Max pixel width for the largest disk
    base_width = max_disk_width + 60
    
    # Create CSS for the game board
    st.markdown("""
<style>
    body {
    background-color: #1e1e1e;
}

.game-board {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    padding: 20px 0;
    background-color: #1e1e1e;
}

.tower {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0 30px;
    position: relative;
}

.peg {
    width: 10px;
    background: linear-gradient(180deg, #ff4e50, #6b5b95);
    border-radius: 5px;
    margin-bottom: 10px;
}

.disk {
    border-radius: 20px;
    text-align: center;
    color: white;
    font-weight: bold;
    height: 28px;
    line-height: 28px;
    box-shadow: 0 0 6px rgba(0,0,0,0.5);
    margin: 5px 0;
    transition: all 0.3s ease;
}

.base {
    background: linear-gradient(90deg, #ff4e50, #6b5b95);
    height: 12px;
    border-radius: 6px;
    margin-top: 10px;
}

.tower-label {
    color: white;
    font-size: 20px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)
    
    # Draw the board
    cols = st.columns(pegs)
    peg_names = ['A', 'B', 'C', 'D'][:pegs]
    
    for i, peg in enumerate(peg_names):
        with cols[i]:
            tower_html = f'<div class="tower" id="peg-{peg}">'
            
            # Calculate peg height based on number of disks
            peg_height = (n * 30) + 20
            tower_html += f'<div class="peg" style="height: {peg_height}px;"></div>'
            
            # Add disks
            for disk in reversed(state[peg]):
                # Calculate disk width proportional to its size
                disk_width = 40 + ((disk / n) * max_disk_width)
                # Generate a color based on disk size
                hue = int(120 + (240 * (disk / n)))
                tower_html += f'<div class="disk dragdrop" id="disk-{disk}" style="width: {disk_width+20}px; background-color: hsl({hue}, 70%, 50%);">{disk}</div>'
            
            # Add base
            tower_html += f'<div class="base" style="width: {base_width}px;"></div>'
            tower_html += f'<div style="text-align: center; margin-top: 10px;"><h2>{peg}</h2></div>'
            tower_html += '</div>'
            
            st.markdown(tower_html, unsafe_allow_html=True)