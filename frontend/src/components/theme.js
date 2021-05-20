import { createMuiTheme } from '@material-ui/core/styles';
import { red } from '@material-ui/core/colors';

const theme = createMuiTheme({
    palette: {
        type: 'dark',
        primary: {
            main: "#2A2A2A",
        },
        secondary: {
            main: "#e2b714",
        },
        error: {
            main: red.A400,
        },
        background: {
            default: "#1E1E1E",
        },
    },
});
export default theme;