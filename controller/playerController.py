def playerController(self,event,pygame):
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