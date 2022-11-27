import numpy as np

class Control():
    def __init__(self, vehicle, control_choice = "PID", allocation_choice = "unconstrained"):
        self.allocation = allocation_choice
        self.control_choice = control_choice
        self.vehicle = vehicle
        self.int_x = np.zeros(3,1)

    def step(self, dt):
        self.x = self.vehicle
        
        pass

    def reference_model(x, omega, zeta):
        pass

    def set_PID(self, Kp, Kd, Ki):
        self.Kp = Kp
        self.Kd = Kd
        self.Ki = Ki

    def controller(self, tau_d):
        if self.control_choice == "PID":
            self.int_x = self.int_x + self.x[0:3]*dt
            tau = -self.Kp*self.eta - self.Kd*self.nu - self.Ki*self.int_x

        elif self.control_choice == "DP":
            pass

    def unconstrained_allocation(self, tau_d):
        B = self.vehicle.B_config
        moore = B.T.dot(B.dot(B.T))
        u = moore*tau_d

        return u