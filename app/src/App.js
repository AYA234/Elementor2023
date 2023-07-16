import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Routing } from './components/routing';
import str from './redux/store';
import { Provider } from 'react-redux';

function App() {

  const darkTheme = createTheme({
    palette: {
      mode: 'dark',
    },
  });

  return (
    <Provider store={str}>
      <ThemeProvider theme={darkTheme}>
        <div className="App">
          <Routing />
        </div>
      </ThemeProvider>
    </Provider>
  );
}

export default App;
