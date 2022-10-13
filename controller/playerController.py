def playerController(self,event,pygame):
    """
    If the game is not paused, and the user presses a key, then the mainTetronomo moves in the direction
    of the key pressed, and if the mainTetronomo is not in a free space, then it moves back to its
    original position.
    
    :param event: The event that was passed to the function
    :param pygame: The pygame module
    """
    if  self.pause == False:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.mainTetronomo.x -= 1
                if not (self.freeSpace()):
                    self.mainTetronomo.x += 1
            if event.key == pygame.K_RIGHT:
                self.mainTetronomo.x += 1
                if not (self.freeSpace()):
                    self.mainTetronomo.x -= 1
            if event.key == pygame.K_DOWN:
                self.mainTetronomo.y += 1
                if not (self.freeSpace()):
                    self.mainTetronomo.y -= 1
            if event.key == pygame.K_UP:
                self.mainTetronomo.rotation += 1
                if not (self.freeSpace()):
                    self.mainTetronomo.rotation -= 1