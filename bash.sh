pip install streamlit-aggrid
# Step 1: Install dependencies
pip install streamlit sqlalchemy psycopg2-binary bcrypt python-dotenv pillow

# Step 2: Create .env
DATABASE_URL=postgresql+psycopg2://youruser:yourpass@localhost:5432/zetachat
SECRET_KEY=your_super_secret_key

# Step 3: Run the app
streamlit run streamlit_app.py

python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-zetachat

python -m twine upload --repository testpypi dist/*
installer -pkg swiftly-1.0.0.pkg -target CurrentUserHomeDirectory
