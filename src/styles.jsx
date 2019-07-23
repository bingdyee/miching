import { makeStyles } from '@material-ui/styles';

const useStyles = makeStyles({
  '@global': {
    '*': {
      color: 'red',
      padding: 0,
      margin: 0,
      border: 0,
      fontSize: '100%',
      font: 'inherit',
      verticalAlign: 'baseline',
      color: 'white',
      height: 'auto'
    },
    'body': {
      background: 'url(/assets/bg.jpg) no-repeat fixed',
      backgroundSize: '100% 100%',
      backgroundPosition: '0 0',
    }
  },
});

export default useStyles;