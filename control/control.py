import numpy as np

class Control():
    """
    Takes vehicle, control choice and 
    """
    def __init__(self, vehicle, control_choice = "PID", allocation_choice = "unconstrained"):
        self.allocation = allocation_choice
        self.control_choice = control_choice
        self.vehicle = vehicle
        self.int_x = np.zeros(3,1)

    def step(self, dt):
        tau = self.controller(dt)
        u = self.allocation(tau)
        self.x = self.vehicle.step(u, dt)
        
        pass

    def reference_model(x, omega, zeta):
        pass

    def set_PID(self, Kp, Kd, Ki):
        self.Kp = Kp
        self.Kd = Kd
        self.Ki = Ki

    def controller(self, dt):
        if self.control_choice == "PID":
            self.int_x = self.int_x + self.x[0:3]*dt
            return -self.Kp*self.eta - self.Kd*self.nu - self.Ki*self.int_x

        elif self.control_choice == "DP":
            pass

    def allocation(self, tau_d):
        if self.allocation_choice == "unconstrained":
            return self.unconstrained_allocation(tau_d)
        
        elif self.allocation_choice == "optimal":
            pass

    def unconstrained_allocation(self, tau_d):
        B = self.vehicle.B_config
        moore_penrose = B.T.dot(B.dot(B.T))
        u = moore_penrose*tau_d

        return u