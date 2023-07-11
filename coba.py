import streamlit as st

def main():
    st.title("Card Button")

    # Card 1
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.markdown(
            """
            [![Card 1](https://via.placeholder.com/150)](https://www.example.com)
            """
        )
    with col2:
        st.markdown(
            """
            [![Card 2](https://via.placeholder.com/150)](https://www.example.com)
            """
        )
    with col3:
        st.markdown(
            """
            [![Card 3](https://via.placeholder.com/150)](https://www.example.com)
            """
        )

    # Card 2
    col4, col5, col6 = st.beta_columns(3)
    with col4:
        st.markdown(
            """
            [![Card 4](https://via.placeholder.com/150)](https://www.example.com)
            """
        )
    with col5:
        st.markdown(
            """
            [![Card 5](https://via.placeholder.com/150)](https://www.example.com)
            """
        )
    with col6:
        st.markdown(
            """
            [![Card 6](https://via.placeholder.com/150)](https://www.example.com)
            """
        )

if __name__ == "__main__":
    main()
