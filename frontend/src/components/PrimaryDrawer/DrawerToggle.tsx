import { ChevronLeft, ChevronRight } from "@mui/icons-material";
import { Box, IconButton } from "@mui/material";

const DrawerToggle: React.FC<Props> = ({
  open,
  handleDrawerClose,
  handleDrawerOpen,
}) => {
  return (
    <Box
      sx={{
        height: "50px",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <IconButton onClick={open ? handleDrawerClose : handleDrawerOpen}>
        {open ? <ChevronLeft /> : <ChevronRight />}
      </IconButton>
    </Box>
  );
};

type Props = {
  open: boolean;
  handleDrawerClose: () => void;
  handleDrawerOpen: () => void;
};

export default DrawerToggle;
